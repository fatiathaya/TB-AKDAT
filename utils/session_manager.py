"""
Session state management for ForestCal application
"""
import streamlit as st


def initialize_session_state():
    """Initialize all session state variables"""
    if 'page' not in st.session_state:
        st.session_state.page = 'Home'
    
    if 'df' not in st.session_state:
        st.session_state.df = None
    
    if 'df_processed' not in st.session_state:
        st.session_state.df_processed = None
    
    if 'pipeline' not in st.session_state:
        st.session_state.pipeline = None
    
    if 'target_col' not in st.session_state:
        st.session_state.target_col = None
    
    if 'feature_cols' not in st.session_state:
        st.session_state.feature_cols = None
    
    if 'missing_strategy' not in st.session_state:
        st.session_state.missing_strategy = 'drop rows'
    
    if 'scaling_option' not in st.session_state:
        st.session_state.scaling_option = True
    
    if 'random_state' not in st.session_state:
        st.session_state.random_state = 42


def navigate_to(page_name):
    """Navigate to a specific page"""
    st.session_state.page = page_name
    st.rerun()


def get_session_value(key, default=None):
    """Safely get value from session state"""
    return st.session_state.get(key, default)


def set_session_value(key, value):
    """Set value in session state"""
    st.session_state[key] = value

