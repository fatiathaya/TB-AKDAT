"""
Home page for ForestCal application
"""
import streamlit as st
from utils.session_manager import navigate_to


def render_home_page():
    """Render the Home page"""
    
    # Hero Section
    st.markdown("""
    <div style="text-align: center; padding: 3rem 0 2rem 0;">
        <h1 style="font-size: 5rem; font-weight: 900; background: linear-gradient(135deg, #a78bfa 0%, #ec4899 100%); 
                   -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 1.5rem;
                   letter-spacing: -0.02em; line-height: 1.1;">
            ForestCal
        </h1>
        <h2 style="font-size: 1.8rem; font-weight: 600; color: white; margin-bottom: 1.5rem;">
            Analisis dan Prediksi Pembakaran Kalori
        </h2>
        <p style="font-size: 1.1rem; color: rgba(255,255,255,0.8); max-width: 800px; margin: 0 auto; line-height: 1.8;">
            Aplikasi berbasis Machine Learning untuk memprediksi pembakaran kalori berdasarkan aktivitas fisik 
            menggunakan algoritma Random Forest Regressor
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Main CTA Button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Mulai Analisis", use_container_width=True, type="primary", key="start_analysis"):
            navigate_to('Dataset')
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Feature Cards
    st.markdown("""
    <h2 style="color: white; font-weight: 600; margin-bottom: 2rem; font-size: 2rem;">
        Fitur Utama
    </h2>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style="background: linear-gradient(135deg, rgba(139, 92, 246, 0.15), rgba(236, 72, 153, 0.1)); 
                    border: 1px solid rgba(139, 92, 246, 0.3); border-radius: 16px; padding: 2rem; height: 250px;
                    border-top: 4px solid #8b5cf6;">
            <h3 style="color: white; text-align: center; margin-bottom: 1rem; font-size: 1.3rem; font-weight: 600;">Upload Dataset</h3>
            <p style="color: rgba(255,255,255,0.8); text-align: center; font-size: 0.95rem; line-height: 1.6;">
                Upload file CSV dengan data aktivitas fisik Anda untuk analisis dan prediksi kalori
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background: linear-gradient(135deg, rgba(139, 92, 246, 0.15), rgba(236, 72, 153, 0.1)); 
                    border: 1px solid rgba(139, 92, 246, 0.3); border-radius: 16px; padding: 2rem; height: 250px;
                    border-top: 4px solid #8b5cf6;">
            <h3 style="color: white; text-align: center; margin-bottom: 1rem; font-size: 1.3rem; font-weight: 600;">Machine Learning</h3>
            <p style="color: rgba(255,255,255,0.8); text-align: center; font-size: 0.95rem; line-height: 1.6;">
                Model Random Forest dengan hyperparameter tuning untuk akurasi prediksi yang optimal
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style="background: linear-gradient(135deg, rgba(139, 92, 246, 0.15), rgba(236, 72, 153, 0.1)); 
                    border: 1px solid rgba(139, 92, 246, 0.3); border-radius: 16px; padding: 2rem; height: 250px;
                    border-top: 4px solid #8b5cf6;">
            <h3 style="color: white; text-align: center; margin-bottom: 1rem; font-size: 1.3rem; font-weight: 600;">Visualisasi</h3>
            <p style="color: rgba(255,255,255,0.8); text-align: center; font-size: 0.95rem; line-height: 1.6;">
                Visualisasi interaktif untuk memahami hasil prediksi dan performa model dengan detail
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # How It Works Section
    st.markdown("""
    <h2 style="color: white; font-weight: 600; margin-bottom: 2rem; font-size: 2rem;">
        Cara Kerja
    </h2>
    """, unsafe_allow_html=True)
    
    steps_col1, steps_col2 = st.columns(2)
    
    with steps_col1:
        st.markdown("""
        <div style="background: rgba(139, 92, 246, 0.1); border-left: 4px solid #8b5cf6; 
                    border-radius: 8px; padding: 1.5rem; margin-bottom: 1rem;">
            <h4 style="color: #a78bfa; margin-bottom: 0.5rem; font-weight: 600;">01. Upload Data</h4>
            <p style="color: rgba(255,255,255,0.8); margin: 0; font-size: 0.95rem;">
                Upload dataset CSV yang berisi informasi aktivitas fisik seperti durasi, intensitas, BMI, dan lainnya
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style="background: rgba(139, 92, 246, 0.1); border-left: 4px solid #8b5cf6; 
                    border-radius: 8px; padding: 1.5rem; margin-bottom: 1rem;">
            <h4 style="color: #a78bfa; margin-bottom: 0.5rem; font-weight: 600;">02. Preprocessing</h4>
            <p style="color: rgba(255,255,255,0.8); margin: 0; font-size: 0.95rem;">
                Pilih target dan fitur yang akan digunakan untuk prediksi, lalu lakukan data cleaning
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style="background: rgba(139, 92, 246, 0.1); border-left: 4px solid #8b5cf6; 
                    border-radius: 8px; padding: 1.5rem;">
            <h4 style="color: #a78bfa; margin-bottom: 0.5rem; font-weight: 600;">03. Training</h4>
            <p style="color: rgba(255,255,255,0.8); margin: 0; font-size: 0.95rem;">
                Atur hyperparameter Random Forest dan latih model untuk mendapatkan akurasi terbaik
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with steps_col2:
        st.markdown("""
        <div style="background: rgba(139, 92, 246, 0.1); border-left: 4px solid #8b5cf6; 
                    border-radius: 8px; padding: 1.5rem; margin-bottom: 1rem;">
            <h4 style="color: #a78bfa; margin-bottom: 0.5rem; font-weight: 600;">04. Visualisasi</h4>
            <p style="color: rgba(255,255,255,0.8); margin: 0; font-size: 0.95rem;">
                Lihat hasil prediksi vs aktual, distribusi residual, dan feature importance dalam bentuk chart
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style="background: rgba(139, 92, 246, 0.1); border-left: 4px solid #8b5cf6; 
                    border-radius: 8px; padding: 1.5rem; margin-bottom: 1rem;">
            <h4 style="color: #a78bfa; margin-bottom: 0.5rem; font-weight: 600;">05. Prediksi</h4>
            <p style="color: rgba(255,255,255,0.8); margin: 0; font-size: 0.95rem;">
                Gunakan model untuk memprediksi pembakaran kalori berdasarkan data aktivitas pribadi Anda
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style="background: rgba(139, 92, 246, 0.1); border-left: 4px solid #8b5cf6; 
                    border-radius: 8px; padding: 1.5rem;">
            <h4 style="color: #a78bfa; margin-bottom: 0.5rem; font-weight: 600;">06. Download</h4>
            <p style="color: rgba(255,255,255,0.8); margin: 0; font-size: 0.95rem;">
                Download hasil prediksi dalam format CSV untuk analisis lebih lanjut
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Tech Stack Section with Images
    st.markdown("""
    <h2 style="color: white; font-weight: 600; margin-bottom: 2rem; font-size: 2rem;">
        Teknologi yang Digunakan
    </h2>
    """, unsafe_allow_html=True)
    
    tech_col1, tech_col2, tech_col3, tech_col4 = st.columns(4)
    
    with tech_col1:
        st.markdown("""
        <div style="text-align: center; padding: 1.5rem; background: rgba(139, 92, 246, 0.1); 
                    border-radius: 12px; min-height: 200px; display: flex; flex-direction: column; 
                    justify-content: center; align-items: center; border: 1px solid rgba(139, 92, 246, 0.2);">
            <img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" 
                 alt="Python" style="width: 80px; height: 80px; margin-bottom: 1rem;">
            <p style="color: white; font-weight: 600; margin: 0; font-size: 1.1rem;">Python</p>
            <p style="color: rgba(255,255,255,0.6); font-size: 0.85rem; margin: 0.5rem 0 0 0;">Core Language</p>
        </div>
        """, unsafe_allow_html=True)
    
    with tech_col2:
        st.markdown("""
        <div style="text-align: center; padding: 1.5rem; background: rgba(139, 92, 246, 0.1); 
                    border-radius: 12px; min-height: 200px; display: flex; flex-direction: column; 
                    justify-content: center; align-items: center; border: 1px solid rgba(139, 92, 246, 0.2);">
            <img src="https://streamlit.io/images/brand/streamlit-mark-color.png" 
                 alt="Streamlit" style="width: 80px; height: 80px; margin-bottom: 1rem;">
            <p style="color: white; font-weight: 600; margin: 0; font-size: 1.1rem;">Streamlit</p>
            <p style="color: rgba(255,255,255,0.6); font-size: 0.85rem; margin: 0.5rem 0 0 0;">Web Framework</p>
        </div>
        """, unsafe_allow_html=True)
    
    with tech_col3:
        st.markdown("""
        <div style="text-align: center; padding: 1.5rem; background: rgba(139, 92, 246, 0.1); 
                    border-radius: 12px; min-height: 200px; display: flex; flex-direction: column; 
                    justify-content: center; align-items: center; border: 1px solid rgba(139, 92, 246, 0.2);">
            <div style="width: 80px; height: 80px; display: flex; align-items: center; justify-content: center; 
                        background: linear-gradient(135deg, #8b5cf6, #ec4899); border-radius: 12px; margin-bottom: 1rem;">
                <span style="color: white; font-size: 2.5rem; font-weight: 700;">RF</span>
            </div>
            <p style="color: white; font-weight: 600; margin: 0; font-size: 1.1rem;">Random Forest</p>
            <p style="color: rgba(255,255,255,0.6); font-size: 0.85rem; margin: 0.5rem 0 0 0;">ML Algorithm</p>
        </div>
        """, unsafe_allow_html=True)
    
    with tech_col4:
        st.markdown("""
        <div style="text-align: center; padding: 1.5rem; background: rgba(139, 92, 246, 0.1); 
                    border-radius: 12px; min-height: 200px; display: flex; flex-direction: column; 
                    justify-content: center; align-items: center; border: 1px solid rgba(139, 92, 246, 0.2);">
            <img src="https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg" 
                 alt="Scikit-learn" style="width: 80px; height: auto; margin-bottom: 1rem;">
            <p style="color: white; font-weight: 600; margin: 0; font-size: 1.1rem;">Scikit-learn</p>
            <p style="color: rgba(255,255,255,0.6); font-size: 0.85rem; margin: 0.5rem 0 0 0;">ML Library</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Call to Action Footer
    st.markdown("""
    <div style="text-align: center; padding: 2rem; background: linear-gradient(135deg, rgba(139, 92, 246, 0.2), rgba(236, 72, 153, 0.15)); 
                border-radius: 16px; margin-top: 2rem;">
        <h3 style="color: white; margin-bottom: 1rem; font-weight: 600;">Siap Memulai?</h3>
        <p style="color: rgba(255,255,255,0.8); margin-bottom: 1.5rem; font-size: 1rem;">
            Mulai analisis pembakaran kalori Anda sekarang dengan ForestCal
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Upload Dataset Sekarang", use_container_width=True, type="primary", key="upload_now"):
            navigate_to('Dataset')
