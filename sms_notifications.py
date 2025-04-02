"""
Module to handle SMS notifications for the Python learning tracker.
"""
import os
from datetime import datetime, timedelta
from twilio.rest import Client
import streamlit as st

# Global settings
DEFAULT_REMINDER_TIME = "09:00"  # 9:00 AM
DEFAULT_REMINDER_MESSAGE = "Remember to practice Python today! Your scheduled topic: {topic}"


def setup_twilio_client():
    """
    Set up and return the Twilio client with credentials.
    Returns None if credentials are missing.
    """
    account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
    auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
    
    if not account_sid or not auth_token:
        return None
    
    return Client(account_sid, auth_token)


def send_sms(phone_number, message):
    """
    Send an SMS to the given phone number with the specified message.
    
    Args:
        phone_number: The recipient's phone number (format: +1XXXXXXXXXX)
        message: The message to send
        
    Returns:
        True if successful, False otherwise
    """
    client = setup_twilio_client()
    twilio_phone = os.environ.get("TWILIO_PHONE_NUMBER")
    
    if not client or not twilio_phone:
        st.error("Twilio not configured. Please add TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, and TWILIO_PHONE_NUMBER to environment variables.")
        return False
    
    try:
        client.messages.create(
            body=message,
            from_=twilio_phone,
            to=phone_number
        )
        return True
    except Exception as e:
        st.error(f"Failed to send SMS: {str(e)}")
        return False


def send_reminder(phone_number, day_info):
    """
    Send a reminder SMS about today's Python learning topic.
    
    Args:
        phone_number: The recipient's phone number
        day_info: Information about the day's topic
        
    Returns:
        True if successful, False otherwise
    """
    # Prepare the message
    message = DEFAULT_REMINDER_MESSAGE.format(topic=day_info['topic'])
    
    # Send the SMS
    return send_sms(phone_number, message)


def send_missed_day_notification(phone_number, day_info):
    """
    Send a notification when a day of learning is missed.
    
    Args:
        phone_number: The recipient's phone number
        day_info: Information about the missed day
        
    Returns:
        True if successful, False otherwise
    """
    message = f"You missed your Python practice yesterday! Today's topic: {day_info['topic']}. Don't break your streak!"
    return send_sms(phone_number, message)


def check_and_send_daily_reminder(phone_number, reminder_time, day_info):
    """
    Check if it's time to send a daily reminder and send if needed.
    
    Args:
        phone_number: The recipient's phone number
        reminder_time: The time to send the reminder (format: "HH:MM")
        day_info: Information about the day's topic
        
    Returns:
        True if reminder was sent, False otherwise
    """
    now = datetime.now()
    
    # Parse reminder time
    try:
        hour, minute = map(int, reminder_time.split(':'))
        reminder_datetime = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
        
        # Check if it's time to send the reminder (within the last 5 minutes)
        time_diff = (now - reminder_datetime).total_seconds()
        if 0 <= time_diff < 300:  # Within 5 minutes after reminder time
            return send_reminder(phone_number, day_info)
    except (ValueError, AttributeError):
        pass
    
    return False


def check_for_missed_days(phone_number, progress_data, current_day_info):
    """
    Check if any days were missed and send notifications.
    
    Args:
        phone_number: The recipient's phone number
        progress_data: The progress data for all days
        current_day_info: Information about the current day
        
    Returns:
        True if notification was sent, False otherwise
    """
    now = datetime.now()
    yesterday = (now - timedelta(days=1)).date()
    
    # Find yesterday's day in the curriculum
    yesterday_idx = None
    for i, day_data in enumerate(progress_data):
        day_scheduled_date = day_data.get('scheduled_date')
        if day_scheduled_date and day_scheduled_date.date() == yesterday:
            yesterday_idx = i
            break
    
    if yesterday_idx is not None:
        # Check if yesterday was completed
        yesterday_completed = progress_data[yesterday_idx].get('completed', False)
        if not yesterday_completed:
            # Send notification about missed day
            return send_missed_day_notification(phone_number, current_day_info)
    
    return False