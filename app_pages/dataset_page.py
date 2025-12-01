"""
Dataset page for ForestCal application
"""
import streamlit as st
from utils.data_handler import load_dataset, validate_dataset
from utils.session_manager import navigate_to


def render_dataset_page():
    """Render the Dataset page"""
    st.title("Upload Dataset")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### Upload Dataset")
        st.markdown("File should be CSV")
        
        # Upload area
        uploaded_file = st.file_uploader(
            "Drag & Drop your files here",
            type=["csv"],
            help="Upload file CSV dengan maksimal 200MB",
            key="dataset_upload"
        )
        
        # Load dataset
        df, message, msg_type = load_dataset(uploaded_file)
        
        if message:
            if msg_type == "success":
                st.success(message)
            elif msg_type == "error":
                st.error(message)
            elif msg_type == "info":
                st.info(message)
        
        # Store in session state
        if df is not None:
            st.session_state.df = df
    
    with col2:
        st.markdown("### Ketentuan Dataset")
        
        # Info boxes
        st.markdown("""
        <div class="info-box">
            <p>📄 CSV Only</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="info-box">
            <p>💾 Maximal 200MB</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="info-box">
            <p>🔤 UTF-8 recommended</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Data exploration
    if st.session_state.df is not None:
        df = st.session_state.df
        
        st.markdown("### Eksplorasi Data Awal")
        st.dataframe(df.head(10), use_container_width=True)
        
        # Data info
        col_info1, col_info2, col_info3 = st.columns(3)
        with col_info1:
            st.metric("Jumlah Baris", len(df))
        with col_info2:
            st.metric("Jumlah Kolom", len(df.columns))
        with col_info3:
            st.metric("Missing Values", df.isnull().sum().sum())
        
        # Next Step
        st.markdown("### Next Step")
        if st.button("Preprocessing Data", use_container_width=True, type="primary"):
            navigate_to('Preprocessing')
    else:
        st.info("👆 Silakan upload dataset CSV untuk melanjutkan")

