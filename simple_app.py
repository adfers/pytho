"""
Super simple Streamlit app - bare minimum to test if it works
"""
import streamlit as st

st.title("Hello World")
st.write("If you can see this, the Streamlit app is working!")

st.markdown("---")
st.subheader("Test Button")
if st.button("Click Me"):
    st.success("Button clicked!")