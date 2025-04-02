"""
Simple debugging script to test visualizations separately.
"""
import sys
import traceback
import json
import os

# Initialize default data
data = {
    "progress": {},
    "notes": {},
    "uploads": {},
    "time_spent": {},
    "resources_used": {}
}

print("Checking imports...")
try:
    import streamlit as st
    import pandas as pd
    import plotly.express as px
    import plotly.graph_objects as go
    import matplotlib.pyplot as plt
    from datetime import datetime, timedelta
    import numpy as np
    print("All imports successful!")
except ImportError as e:
    print(f"Import error: {e}")
    traceback.print_exc()
    sys.exit(1)

print("Testing visualization functions...")
import visualizations as viz

# Test basic plotting function
def test_completion_gauge():
    print("Testing completion gauge...")
    try:
        fig = viz.create_completion_gauge(25.0)
        print("Completion gauge created successfully")
        return True
    except Exception as e:
        print(f"Error creating completion gauge: {e}")
        traceback.print_exc()
        return False

# Test weekly progress chart
def test_weekly_progress():
    print("Testing weekly progress chart...")
    try:
        weekly_progress = [2, 1, 0]  # Simple test data
        fig = viz.create_weekly_progress_chart(weekly_progress)
        print("Weekly progress chart created successfully")
        return True
    except Exception as e:
        print(f"Error creating weekly progress chart: {e}")
        traceback.print_exc()
        return False

# Test progress heatmap
def test_progress_heatmap():
    print("Testing progress heatmap...")
    try:
        # Create simple test data for 21 days
        progress_data = []
        for day in range(1, 22):
            progress_data.append({
                'day': day,
                'completed': day <= 3,  # Mark first 3 days as completed
                'completion_date': '2025-03-29' if day <= 3 else None,
                'time_spent_minutes': 60 if day <= 3 else 0
            })
        
        fig = viz.create_progress_heatmap(progress_data)
        print("Progress heatmap created successfully")
        return True
    except Exception as e:
        print(f"Error creating progress heatmap: {e}")
        traceback.print_exc()
        return False

# Run all tests
if __name__ == "__main__":
    test_results = {
        "completion_gauge": test_completion_gauge(),
        "weekly_progress": test_weekly_progress(),
        "progress_heatmap": test_progress_heatmap()
    }
    
    print("\nTest Results:")
    for test, result in test_results.items():
        print(f"{test}: {'✅ Passed' if result else '❌ Failed'}")
    
    if all(test_results.values()):
        print("\nAll visualization tests passed successfully!")
    else:
        print("\nSome visualization tests failed. Check the logs above for details.")