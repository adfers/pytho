"""
Debugging script for utils.py
"""
import sys
import traceback
import json
import os
from datetime import datetime

# Create a simple test data file
TEST_DATA_FILE = "test_progress.json"

def create_test_data():
    data = {
        "progress": {
            "1": {
                "completed": True,
                "date_completed": datetime.now().strftime("%Y-%m-%d")
            },
            "2": {
                "completed": True,
                "date_completed": datetime.now().strftime("%Y-%m-%d")
            }
        },
        "notes": {"1": "Test note"},
        "uploads": {},
        "time_spent": {"1": 60, "2": 120},
        "resources_used": {"1": ["W3Schools"]}
    }
    
    with open(TEST_DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)
    
    return data

# Patch data_handler to use test data
import data_handler as dh
original_data_file = dh.DATA_FILE
dh.DATA_FILE = TEST_DATA_FILE

# Create test data
print("Creating test data...")
test_data = create_test_data()
print("Test data created")

# Testing utils functions
print("\nTesting utility functions...")
import utils

# Test get_current_day
print("Testing get_current_day()...")
try:
    current_day = utils.get_current_day()
    print(f"Current day: {current_day}")
except Exception as e:
    print(f"Error in get_current_day(): {e}")
    traceback.print_exc()

# Test format_time_display
print("\nTesting format_time_display()...")
try:
    for minutes in [30, 60, 90, 120]:
        formatted = utils.format_time_display(minutes)
        print(f"{minutes} minutes -> {formatted}")
except Exception as e:
    print(f"Error in format_time_display(): {e}")
    traceback.print_exc()

# Test learning streak calculation
print("\nTesting calculate_learning_streak()...")
try:
    streak = utils.calculate_learning_streak()
    print(f"Learning streak: {streak}")
except Exception as e:
    print(f"Error in calculate_learning_streak(): {e}")
    traceback.print_exc()

# Clean up
print("\nCleaning up...")
try:
    os.remove(TEST_DATA_FILE)
    print("Test data file removed")
except:
    print("Failed to remove test data file")

# Restore original data file
dh.DATA_FILE = original_data_file
print("Original data file path restored")
print("Debugging complete")