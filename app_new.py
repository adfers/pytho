def show_email_settings():
    """Display email notification settings."""
    st.header("Email Reminder Settings")
    
    # Get current settings from session state or initialize
    if 'email' not in st.session_state:
        st.session_state.email = ""
    if 'email_enabled' not in st.session_state:
        st.session_state.email_enabled = False
    if 'reminder_time' not in st.session_state:
        st.session_state.reminder_time = "09:00"  # Default 9:00 AM
    if 'missed_day_notification' not in st.session_state:
        st.session_state.missed_day_notification = True
    if 'daily_reminder' not in st.session_state:
        st.session_state.daily_reminder = True
    
    # Load saved settings
    data = dh.load_data()
    email_settings = data.get("email_settings", {})
    
    if email_settings:
        st.session_state.email_enabled = email_settings.get("enabled", False)
        st.session_state.email = email_settings.get("email", "")
        st.session_state.reminder_time = email_settings.get("reminder_time", "09:00")
        st.session_state.missed_day_notification = email_settings.get("missed_day_notification", True)
        st.session_state.daily_reminder = email_settings.get("daily_reminder", True)
    
    # Email Settings form
    with st.form("email_settings_form"):
        st.subheader("Email Notification Preferences")
        
        # Enable/disable email notifications
        email_enabled = st.checkbox("Enable email notifications", value=st.session_state.email_enabled)
        
        # Email address input
        email = st.text_input("Your email address:", value=st.session_state.email)
        
        # Daily reminder time
        st.subheader("Notification Schedule")
        
        # Time selection
        time_parts = st.session_state.reminder_time.split(":")
        hour = int(time_parts[0])
        minute = int(time_parts[1])
        
        time_col1, time_col2 = st.columns(2)
        with time_col1:
            reminder_hour = st.selectbox("Hour:", list(range(0, 24)), index=hour)
        with time_col2:
            reminder_minute = st.selectbox("Minute:", list(range(0, 60, 5)), index=minute // 5)
        
        # Notification types
        st.subheader("Notification Types")
        daily_reminder = st.checkbox("Daily reminders", value=st.session_state.daily_reminder, 
                                help="Get a daily reminder about your scheduled Python topic")
        missed_day = st.checkbox("Missed day notifications", value=st.session_state.missed_day_notification,
                            help="Get notified when you miss a day of practice")
        
        # Submit button
        submit_button = st.form_submit_button("Save Settings")
        
        if submit_button:
            # Format time as HH:MM
            reminder_time_str = f"{reminder_hour:02d}:{reminder_minute:02d}"
            
            # Save settings to data file
            data = dh.load_data()
            data["email_settings"] = {
                "enabled": email_enabled,
                "email": email,
                "reminder_time": reminder_time_str,
                "missed_day_notification": missed_day,
                "daily_reminder": daily_reminder
            }
            dh.save_data(data)
            
            # Update session state
            st.session_state.email_enabled = email_enabled
            st.session_state.email = email
            st.session_state.reminder_time = reminder_time_str
            st.session_state.missed_day_notification = missed_day
            st.session_state.daily_reminder = daily_reminder
            
            st.success("Email settings saved successfully!")
    
    # Test email notification (if enabled)
    if st.session_state.email_enabled and st.session_state.email:
        st.subheader("Test Email Notification")
        
        test_col1, test_col2 = st.columns([3, 1])
        with test_col1:
            test_message = st.text_input("Test message:", value="This is a test from Python Learning Tracker!")
        
        with test_col2:
            if st.button("Send Test"):
                if email_notifications.send_email(st.session_state.email, "Python Learning Tracker - Test", f"<p>{test_message}</p>"):
                    st.success("Test email sent successfully!")
                else:
                    st.error("Failed to send test email. Please check your email address and try again.")
    
    # Information about email notifications
    with st.expander("About Email Notifications"):
        st.markdown("""
        **How email notifications work:**
        
        - **Daily Reminders**: You'll receive an email at your set time with information about the day's Python learning topic.
        - **Missed Day Alerts**: If you don't mark a day as completed, you'll receive a reminder the next day.
        
        **Note**: Emails are sent from the Python Learning Tracker application. Make sure to check your spam folder if you don't see them in your inbox.
        """)