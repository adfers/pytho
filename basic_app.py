"""
Basic version of the Python Learning Tracker to ensure core functionality works
"""
import streamlit as st
import pandas as pd
import json
import os

# Define the data file path
DATA_FILE = "python_learning_progress.json"

def initialize_data():
    """Initialize the data structure if it doesn't exist."""
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r') as f:
                return json.load(f)
        except:
            pass
    
    # Create a default data structure
    data = {
        "progress": {},
        "notes": {},
        "uploads": {},
        "time_spent": {},
        "resources_used": {}
    }
    
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)
    
    return data

# Page configuration
st.set_page_config(
    page_title="Python Learning Tracker",
    page_icon="🐍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Main app
st.title("Python Learning Tracker")
st.subheader("21-Day Python Learning Journey")

# Initialize data
data = initialize_data()

# Simple progress display
st.markdown("## Your Progress")

# Count completed days
completed_days = sum(1 for day in data["progress"].values() if day.get("completed", False))
total_days = 21

# Display progress bar
st.progress(completed_days / total_days)
st.write(f"You've completed {completed_days} out of {total_days} days!")

# Simple day tracker
st.markdown("## Quick Day Tracker")
day_number = st.number_input("Select a day to track:", min_value=1, max_value=21, value=1)

# Check if day is completed
is_completed = str(day_number) in data["progress"] and data["progress"][str(day_number)].get("completed", False)

# Checkbox for completion
completed = st.checkbox("Mark as completed", value=is_completed)

if completed != is_completed:
    if completed:
        # Mark as completed
        from datetime import datetime
        data["progress"][str(day_number)] = {
            "completed": True,
            "date_completed": datetime.now().strftime("%Y-%m-%d")
        }
    else:
        # Mark as incomplete
        if str(day_number) in data["progress"]:
            del data["progress"][str(day_number)]
    
    # Save the data
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)
    
    st.success(f"Day {day_number} marked as {'completed' if completed else 'incomplete'}!")
    st.rerun()

# Display some curriculum information
st.markdown("## About Python Learning Calendar")
st.markdown("""
This app helps you track your progress through a 21-day Python learning journey.
The curriculum covers:

- Week 1: Python Basics (Variables, Operators, Conditions, Loops, Functions, Lists)
- Week 2: Intermediate Python (Dictionaries, Files, Error Handling, Modules, OOP, APIs)  
- Week 3: Advanced Topics & Final Project (Data Structures, Algorithms, Libraries)

Use this tracker to:
1. Mark your daily progress
2. Track time spent on each topic
3. Take notes on what you're learning
4. Plan your learning journey
""")

if st.button("View Full App Features"):
    st.info("The full app includes visualizations, note-taking, weekly view, and more!")