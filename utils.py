"""
Utility functions for the Python learning tracker.
"""
import streamlit as st
from datetime import datetime, timedelta
import curriculum as curr
import data_handler as dh

# Define the start date as tomorrow
START_DATE = (datetime.now() + timedelta(days=1)).date()

def get_current_day():
    """Get the current day in the curriculum based on progress."""
    progress_data = dh.get_all_progress_data()
    
    # Find the first incomplete day
    for day_data in progress_data:
        if not day_data['completed']:
            return day_data['day']
    
    # If all are complete, return the last day
    return 21

def format_time_display(minutes):
    """Format minutes into hours and minutes for display."""
    hours = minutes // 60
    remaining_minutes = minutes % 60
    
    if hours == 0:
        return f"{remaining_minutes} min"
    elif remaining_minutes == 0:
        return f"{hours} hr"
    else:
        return f"{hours} hr {remaining_minutes} min"

def get_day_info(day_number):
    """Get all information about a specific day."""
    curriculum = curr.get_curriculum_data()
    
    # Find the day in the curriculum
    week_index = (day_number - 1) // 7
    day_in_week_index = (day_number - 1) % 7
    
    try:
        week_data = curriculum[week_index]
        day_data = week_data["days"][day_in_week_index]
        
        # Get the scheduled date for this day
        scheduled_date = get_scheduled_date(day_number)
        formatted_date = format_date(scheduled_date)
        
        return {
            "day": day_number,
            "week": week_index + 1,
            "week_title": week_data["title"],
            "topic": day_data["topic"],
            "resources": day_data["resources"],
            "practice": day_data["practice"],
            "scheduled_date": scheduled_date,
            "formatted_date": formatted_date
        }
    except (IndexError, KeyError):
        return None

def get_upcoming_days(current_day, num_days=3):
    """Get information about upcoming days in the curriculum."""
    upcoming = []
    
    for day_num in range(current_day, min(current_day + num_days, 22)):
        day_info = get_day_info(day_num)
        if day_info:
            upcoming.append(day_info)
    
    return upcoming

def calculate_learning_streak():
    """Calculate the current learning streak."""
    try:
        progress_data = dh.get_all_progress_data()
        
        # Get completed days with dates
        completed_days = []
        for d in progress_data:
            try:
                if d.get('completed', False) and d.get('completion_date'):
                    date = datetime.strptime(d['completion_date'], "%Y-%m-%d").date()
                    completed_days.append(date)
            except (ValueError, TypeError):
                # Skip dates that can't be parsed
                continue
        
        if not completed_days:
            return 0
        
        # Sort the dates
        completed_days.sort()
        
        # Check if there's an entry for today
        today = datetime.now().date()
        streak = 1 if today in completed_days else 0
        
        # Count consecutive days backward from the most recent
        check_date = today - timedelta(days=1)
        
        while check_date in completed_days:
            streak += 1
            check_date = check_date - timedelta(days=1)
        
        return streak
    except Exception as e:
        # Return 0 in case of any error
        return 0

def get_total_study_time():
    """Calculate the total study time across all days."""
    try:
        progress_data = dh.get_all_progress_data()
        total_minutes = sum(d.get('time_spent_minutes', 0) for d in progress_data)
        return total_minutes
    except Exception:
        return 0
        
def get_scheduled_date(day_number):
    """Calculate the scheduled date for a specific day in the curriculum.
    
    Args:
        day_number: The day number in the curriculum (1-21)
        
    Returns:
        A date object representing the scheduled date
    """
    if day_number < 1 or day_number > curr.get_days_count():
        return None
    
    # Calculate days offset (day 1 is tomorrow)
    days_offset = day_number - 1
    return START_DATE + timedelta(days=days_offset)

def format_date(date_obj):
    """Format a date object into a readable string.
    
    Args:
        date_obj: A date object
        
    Returns:
        A formatted date string like "Monday, March 30"
    """
    if date_obj is None:
        return "N/A"
    
    return date_obj.strftime("%A, %B %d, %Y")
