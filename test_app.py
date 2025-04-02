"""
Minimal streamlit app to test the issue
"""
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Test App",
    page_icon="🐍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Simple layout
st.title("Python Learning Tracker - Test")
st.write("This is a test app to diagnose loading issues")

# Simple UI elements in sidebar
with st.sidebar:
    st.title("Sidebar")
    st.write("Navigation")
    selected = st.radio("Go to:", ["Home", "About"])

# Main page content
if selected == "Home":
    st.header("Home Page")
    st.write("Welcome to the test app!")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Column 1")
        st.write("Content for column 1")
    with col2:
        st.subheader("Column 2")
        st.write("Content for column 2")
    
    # Add a simple chart
    import pandas as pd
    import numpy as np
    
    data = pd.DataFrame({
        'x': np.arange(10),
        'y': np.random.randn(10)
    })
    
    st.line_chart(data)
    
else:
    st.header("About Page")
    st.write("This is a minimal test app for troubleshooting.")