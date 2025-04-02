"""
Module to handle the data operations for the Python learning tracker.
"""
import json
import os
import time
from datetime import datetime
from functools import lru_cache
import pandas as pd

# Default data file path
DATA_FILE = "python_learning_progress.json"

# Cache settings
DATA_CACHE_TTL = 60  # Cache data for 60 seconds
_data_cache = None
_last_load_time = 0

def initialize_data():
    """Initialize the data structure if it doesn't exist."""
    if os.path.exists(DATA_FILE):
        return load_data()
    
    # Create a default data structure
    data = {
        "progress": {},
        "notes": {},
        "uploads": {},
        "time_spent": {},
        "resources_used": {},
        "sms_settings": {
            "enabled": False,
            "phone_number": "",
            "reminder_time": "09:00",
            "missed_day_notification": True,
            "daily_reminder": True
        }
    }
    
    save_data(data)
    return data

def load_data():
    """Load the data from the JSON file with caching for performance."""
    global _data_cache, _last_load_time
    
    current_time = time.time()
    
    # If we have a valid cache, use it
    if _data_cache is not None and (current_time - _last_load_time) < DATA_CACHE_TTL:
        return _data_cache
    
    try:
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
            _data_cache = data
            _last_load_time = current_time
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        # If file doesn't exist or is corrupted, initialize a new one
        new_data = initialize_data()
        _data_cache = new_data
        _last_load_time = current_time
        return new_data

# Save throttling
_last_save_time = 0 
SAVE_THROTTLE = 2  # Minimum seconds between saves

def save_data(data):
    """Save the data to the JSON file with throttling."""
    global _data_cache, _last_load_time, _last_save_time
    
    current_time = time.time()
    
    # Update cache immediately
    _data_cache = data
    _last_load_time = current_time
    
    # Throttle saves to prevent excessive disk I/O
    if current_time - _last_save_time < SAVE_THROTTLE:
        return data
    
    try:
        with open(DATA_FILE, 'w') as f:
            json.dump(data, f, indent=4)
        _last_save_time = current_time
    except Exception as e:
        print(f"Error saving data: {e}")
        
    return data

def mark_day_complete(day_number, completed=True):
    """Mark a specific day as completed or incomplete."""
    data = load_data()
    
    if completed:
        data["progress"][str(day_number)] = {
            "completed": True,
            "date_completed": datetime.now().strftime("%Y-%m-%d")
        }
    else:
        # If marking as incomplete, remove the entry if it exists
        if str(day_number) in data["progress"]:
            del data["progress"][str(day_number)]
    
    save_data(data)
    return data

def update_time_spent(day_number, hours, minutes):
    """Update the time spent on a specific day."""
    data = load_data()
    
    total_minutes = hours * 60 + minutes
    data["time_spent"][str(day_number)] = total_minutes
    
    save_data(data)
    return data

def save_note(day_number, note_text):
    """Save a note for a specific day."""
    data = load_data()
    
    data["notes"][str(day_number)] = note_text
    
    save_data(data)
    return data

def get_note(day_number):
    """Get the note for a specific day."""
    data = load_data()
    return data["notes"].get(str(day_number), "")

def mark_resource_used(day_number, resource):
    """Mark a resource as used for a specific day."""
    data = load_data()
    
    if str(day_number) not in data["resources_used"]:
        data["resources_used"][str(day_number)] = []
    
    if resource not in data["resources_used"][str(day_number)]:
        data["resources_used"][str(day_number)].append(resource)
    
    save_data(data)
    return data

def get_resources_used(day_number):
    """Get the resources used for a specific day."""
    data = load_data()
    return data["resources_used"].get(str(day_number), [])

def get_all_progress_data():
    """Get all progress data in a format suitable for visualizations."""
    data = load_data()
    progress = []
    
    for day_num in range(1, 22):  # For all 21 days
        day_str = str(day_num)
        is_completed = day_str in data["progress"] and data["progress"][day_str]["completed"]
        completion_date = data["progress"].get(day_str, {}).get("date_completed", None)
        time_spent = data["time_spent"].get(day_str, 0)  # In minutes
        
        progress.append({
            "day": day_num,
            "completed": is_completed,
            "completion_date": completion_date,
            "time_spent_minutes": time_spent
        })
    
    return progress

def get_completion_percentage():
    """Calculate the percentage of curriculum completed."""
    data = load_data()
    completed_days = sum(1 for day in data["progress"].values() if day.get("completed", False))
    return (completed_days / 21) * 100  # 21 days total

def get_weekly_progress():
    """Get progress data by week."""
    data = load_data()
    weekly_progress = [0, 0, 0]  # 3 weeks
    
    for day_num in range(1, 22):
        day_str = str(day_num)
        if day_str in data["progress"] and data["progress"][day_str]["completed"]:
            # Determine which week this day belongs to
            week_idx = (day_num - 1) // 7
            if week_idx < 3:  # Just to be safe
                weekly_progress[week_idx] += 1
    
    return weekly_progress

def get_time_spent_by_week():
    """Get time spent data by week in hours."""
    data = load_data()
    weekly_time = [0, 0, 0]  # 3 weeks
    
    for day_num in range(1, 22):
        day_str = str(day_num)
        time_spent = data["time_spent"].get(day_str, 0)  # In minutes
        
        # Determine which week this day belongs to
        week_idx = (day_num - 1) // 7
        if week_idx < 3:  # Just to be safe
            weekly_time[week_idx] += time_spent
    
    # Convert minutes to hours
    weekly_time = [time / 60 for time in weekly_time]
    return weekly_time
