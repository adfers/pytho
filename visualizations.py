
"""
Visualization functions for the Python Learning Tracker
"""
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import pandas as pd
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_completion_gauge(percentage):
    """Create a gauge chart showing completion percentage."""
    try:
        percentage = float(percentage)
        percentage = max(0, min(100, percentage))  # Clamp between 0 and 100
            
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=percentage,
            domain={'x': [0, 1], 'y': [0, 1]},
            title={'text': "Completion"},
            number={'suffix': "%"},
            gauge={
                'axis': {'range': [None, 100]},
                'bar': {'color': "#4B89DC"},
                'steps': [
                    {'range': [0, 33], 'color': "#FFE5E5"},
                    {'range': [33, 66], 'color': "#FFD6A5"},
                    {'range': [66, 100], 'color': "#CAFFBF"}
                ]
            }
        ))
        fig.update_layout(height=200, margin=dict(l=10, r=10, t=40, b=10))
        return fig
    except (ValueError, TypeError) as e:
        logger.error(f"Error creating completion gauge: {str(e)}")
        return go.Figure()

def create_weekly_progress_chart(weekly_progress):
    """Create a bar chart showing weekly progress."""
    try:
        if not isinstance(weekly_progress, (list, tuple)):
            raise ValueError("Weekly progress must be a list or tuple")
        
        if not weekly_progress:
            raise ValueError("Weekly progress data is empty")
            
        weeks = [f"Week {i+1}" for i in range(len(weekly_progress))]
        fig = go.Figure(data=[
            go.Bar(
                x=weeks,
                y=weekly_progress,
                marker_color='#4B89DC',
                text=weekly_progress,
                textposition='auto'
            )
        ])
        fig.update_layout(
            title="Weekly Progress",
            xaxis_title="Week",
            yaxis_title="Completed Days",
            height=300
        )
        return fig
    except Exception as e:
        logger.error(f"Error creating weekly progress chart: {str(e)}")
        return go.Figure()

def create_progress_heatmap(progress_data):
    """Create a heatmap showing daily progress."""
    try:
        if not isinstance(progress_data, list):
            raise ValueError("Progress data must be a list")

        # Ensure we have data for all 21 days
        progress_data = progress_data[:21]  # Truncate if too long
        while len(progress_data) < 21:
            progress_data.append({'completed': False})

        days = list(range(1, 22))
        completion = [1 if d.get('completed', False) else 0 for d in progress_data]
        
        fig = px.imshow(
            [completion],
            labels=dict(x="Day", y="Progress", color="Completed"),
            x=days,
            color_continuous_scale=["#FFE5E5", "#4B89DC"]
        )
        fig.update_layout(
            title="Progress Heatmap",
            height=200,
            xaxis_title="Day",
            yaxis_visible=False
        )
        return fig
    except Exception as e:
        logger.error(f"Error creating progress heatmap: {str(e)}")
        return go.Figure()

def create_time_spent_chart(progress_data):
    """Create a line chart showing time spent per day."""
    try:
        if not isinstance(progress_data, list):
            raise ValueError("Progress data must be a list")

        if not progress_data:
            raise ValueError("Progress data is empty")

        days = list(range(1, len(progress_data) + 1))
        times = [d.get('time_spent_minutes', 0) for d in progress_data]
        
        fig = go.Figure(data=go.Scatter(
            x=days,
            y=times,
            mode='lines+markers',
            line=dict(color='#4B89DC')
        ))
        fig.update_layout(
            title="Time Spent Per Day",
            xaxis_title="Day",
            yaxis_title="Minutes",
            height=300
        )
        return fig
    except Exception as e:
        logger.error(f"Error creating time spent chart: {str(e)}")
        return go.Figure()

def create_streak_calendar(progress_data):
    """Create a calendar heatmap showing activity streaks."""
    try:
        if not isinstance(progress_data, list):
            raise ValueError("Progress data must be a list")

        if not progress_data:
            raise ValueError("Progress data is empty")

        dates = []
        values = []
        
        for day in progress_data:
            try:
                completion_date = day.get('completion_date')
                if completion_date:
                    # Validate date format
                    datetime.strptime(completion_date, "%Y-%m-%d")
                    dates.append(completion_date)
                    values.append(1)
            except ValueError as e:
                logger.warning(f"Invalid date format: {completion_date}")
                continue
        
        if dates:
            df = pd.DataFrame({
                'date': dates,
                'value': values
            })
            fig = px.scatter(df, x='date', y='value', color='value')
            fig.update_layout(
                title="Activity Calendar",
                height=200,
                showlegend=False
            )
            return fig
        return go.Figure()
    except Exception as e:
        logger.error(f"Error creating streak calendar: {str(e)}")
        return go.Figure()

def create_weekly_time_chart(weekly_time):
    """Create a bar chart showing time spent by week."""
    try:
        if not isinstance(weekly_time, (list, tuple)):
            raise ValueError("Weekly time must be a list or tuple")
        
        # Ensure we have exactly 3 weeks of data
        weekly_time = list(weekly_time)[:3]  # Take first 3 weeks
        while len(weekly_time) < 3:
            weekly_time.append(0)
            
        weeks = [f"Week {i+1}" for i in range(len(weekly_time))]
        
        # Always convert to hours for consistency
        weekly_time_hours = [t/60 for t in weekly_time]  # Convert all values to hours
        
        fig = go.Figure(data=[
            go.Bar(
                x=weeks,
                y=weekly_time_hours,
                marker_color='#4B89DC',
                text=[f"{t:.1f}h" for t in weekly_time_hours],
                textposition='auto'
            )
        ])
        fig.update_layout(
            title="Time Spent by Week",
            xaxis_title="Week",
            yaxis_title="Hours",
            height=300,
            margin=dict(l=10, r=10, t=40, b=10)
        )
        return fig
    except Exception as e:
        logger.error(f"Error creating weekly time chart: {str(e)}")
        return go.Figure()
