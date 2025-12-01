"""
ForestCal - Aplikasi Analisis dan Prediksi Pembakaran Kalori
Main orchestrator file
"""

import streamlit as st

# Import configuration
from config.settings import PAGE_CONFIG, MENU_ITEMS

# Import utilities
from utils.session_manager import initialize_session_state, navigate_to

# Import styling
from styles.custom_css import get_custom_css

# Import page renderers
from app_pages import (
    render_home_page,
    render_dataset_page,
    render_preprocessing_page,
    render_training_page,
    render_visualization_page,
    render_analysis_page
)


def render_sidebar():
    """Render sidebar navigation"""
    with st.sidebar:
        st.markdown('<div class="logo">ForestCal</div>', unsafe_allow_html=True)
        
        st.markdown("### Menu Utama")
        
        # Main menu items
        for menu_name, icon in MENU_ITEMS.items():
            is_active = st.session_state.page == menu_name
            button_type = "primary" if is_active else "secondary"
            button_text = menu_name.strip()
            if st.button(button_text, key=f"menu_{menu_name}", 
                        use_container_width=True, type=button_type):
                navigate_to(menu_name)
        
        st.markdown("---")
        st.markdown("### Analisis Data Pribadi")
        
        # Personal analysis menu
        is_personal_active = st.session_state.page == 'Analisis Pribadi'
        personal_button_type = "primary" if is_personal_active else "secondary"
        if st.button("Analisis", key="menu_analisis_pribadi", 
                    use_container_width=True, type=personal_button_type):
            navigate_to('Analisis Pribadi')


def render_current_page():
    """Render the current page based on session state"""
    page = st.session_state.page
    
    if page == 'Home':
        render_home_page()
    elif page == 'Dataset':
        render_dataset_page()
    elif page == 'Preprocessing':
        render_preprocessing_page()
    elif page == 'Training Data':
        render_training_page()
    elif page == 'Visualisasi Data':
        render_visualization_page()
    elif page == 'Analisis Pribadi':
        render_analysis_page()
    else:
        st.error(f"Unknown page: {page}")


def main():
    """Main application entry point"""
    # Page configuration
    st.set_page_config(**PAGE_CONFIG)
    
    # Apply custom CSS
    st.markdown(get_custom_css(), unsafe_allow_html=True)
    
    # Initialize session state
    initialize_session_state()
    
    # Render sidebar navigation
    render_sidebar()
    
    # Render main content
    st.markdown('<div class="main-content">', unsafe_allow_html=True)
    render_current_page()
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Footer
    st.markdown("---")
    st.caption('ForestCal - Aplikasi Analisis dan Prediksi Pembakaran Kalori | Dikembangkan untuk tugas mata kuliah')


if __name__ == "__main__":
    main()
