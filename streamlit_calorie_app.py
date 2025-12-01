# Streamlit app: ForestCal - Analisis dan Prediksi Pembakaran Kalori
# Menggunakan Random Forest Regressor
# Cara jalankan: install dependencies dan jalankan `streamlit run streamlit_calorie_app.py`

import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64

st.set_page_config(
    page_title="ForestCal - Prediksi Kalori",
    page_icon="🌲",
    layout="wide",
    initial_sidebar_state="expanded"
)


st.markdown("""
<style>
    /* Main background */
    .stApp {
        background: linear-gradient(135deg, #2d1b4e 0%, #1a0d2e 100%);
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #4a2c7a 0%, #2d1b4e 100%);
    }
    
    [data-testid="stSidebar"] .css-1d391kg {
        padding-top: 0rem;
    }
    
    /* Sidebar menu items */
    .sidebar-menu-item {
        padding: 0.75rem 1rem;
        margin: 0.25rem 0;
        border-radius: 8px;
        cursor: pointer;
        transition: all 0.3s;
        color: white;
        display: flex;
        align-items: center;
        gap: 0.75rem;
    }
    
    .sidebar-menu-item:hover {
        background-color: rgba(255, 255, 255, 0.1);
    }
    
    .sidebar-menu-item.active {
        background-color: rgba(255, 255, 255, 0.2);
        font-weight: bold;
    }
    
    /* Logo */
    .logo {
        font-size: 2rem;
        font-weight: bold;
        color: white;
        text-align: center;
        padding: 1.5rem 0;
        margin-bottom: 2rem;
    }
    
    /* Main content styling */
    .main-content {
        color: white;
    }
    
    /* Section headers */
    h1, h2, h3 {
        color: white !important;
    }
    
    /* Upload area styling */
    .upload-area {
        border: 2px dashed #8b5cf6;
        border-radius: 12px;
        padding: 3rem 2rem;
        text-align: center;
        background-color: rgba(139, 92, 246, 0.1);
        margin: 1rem 0;
        cursor: pointer;
        transition: all 0.3s;
    }
    
    .upload-area:hover {
        background-color: rgba(139, 92, 246, 0.2);
        border-color: #a78bfa;
    }
    
    /* Global button styling (non-sidebar) */
    .stButton>button {
        border-radius: 8px;
        font-weight: 500;
        transition: all 0.25s ease;
    }
    
    .stButton>button:hover {
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.35);
    }
    
    /* Sidebar navigation buttons - modern pill style */
    [data-testid="stSidebar"] .stButton>button {
        width: 100%;
        justify-content: flex-start;
        border-radius: 999px;
        padding: 0.6rem 1rem;
        font-size: 0.95rem;
        border: 1px solid transparent;
        background: transparent;
        color: #e5e7eb;
        box-shadow: none;
    }
    
    [data-testid="stSidebar"] .stButton>button[kind="secondary"] {
        background: linear-gradient(90deg, rgba(148, 163, 184, 0.15), rgba(30, 64, 175, 0.0));
    }
    
    [data-testid="stSidebar"] .stButton>button[kind="secondary"]:hover {
        background: linear-gradient(90deg, rgba(129, 140, 248, 0.45), rgba(59, 130, 246, 0.15));
        border-color: rgba(129, 140, 248, 0.7);
        transform: translateY(-1px);
        box-shadow: 0 8px 18px rgba(15, 23, 42, 0.75);
    }
    
    [data-testid="stSidebar"] .stButton>button[kind="primary"] {
        background: linear-gradient(90deg, #8b5cf6, #ec4899);
        border-color: rgba(248, 250, 252, 0.5);
        color: white;
        box-shadow: 0 10px 25px rgba(139, 92, 246, 0.6);
    }
    
    [data-testid="stSidebar"] .stButton>button[kind="primary"]:hover {
        filter: brightness(1.05);
        transform: translateY(-1px);
        box-shadow: 0 14px 30px rgba(139, 92, 246, 0.9);
    }
    
    /* Table styling */
    .dataframe {
        background-color: white;
        color: black;
    }
    
    /* Info boxes */
    .info-box {
        background-color: rgba(139, 92, 246, 0.2);
        border: 1px solid #8b5cf6;
        border-radius: 8px;
        padding: 1rem;
        margin: 0.5rem 0;
    }
    
    /* Card styling for preprocessing page */
    .preprocessing-card {
        background: linear-gradient(135deg, rgba(139, 92, 246, 0.4) 0%, rgba(124, 58, 237, 0.3) 100%);
        border: 1px solid rgba(139, 92, 246, 0.6);
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1.5rem 0;
        color: white;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    .preprocessing-card h3 {
        color: white !important;
        margin-bottom: 1rem;
        font-size: 1.2rem;
        font-weight: 600;
    }
    
    .preprocessing-card p {
        color: white;
        margin: 0.5rem 0;
        font-size: 1rem;
    }
    
    .preprocessing-card ul {
        color: white;
        margin: 0.5rem 0;
        padding-left: 1.5rem;
    }
    
    .preprocessing-card li {
        color: white;
        margin: 0.25rem 0;
    }
    
    /* Table preview styling */
    .table-preview {
        background-color: white;
        border-radius: 8px;
        padding: 1rem;
        margin: 1rem 0;
        overflow-x: auto;
    }
    
    /* Selectbox inside card */
    .preprocessing-card .stSelectbox {
        margin-top: 1rem;
    }
    
    /* Markdown text inside card */
    .preprocessing-card .stMarkdown {
        color: white;
    }
    
    /* Selectbox styling */
    .stSelectbox > div > div {
        background-color: rgba(139, 92, 246, 0.3);
        border: 1px solid #8b5cf6;
        border-radius: 8px;
    }
    
    /* Checkbox styling */
    .stCheckbox > label {
        color: white;
    }
    
    /* Training page styling */
    .training-section {
        margin: 2rem 0;
        padding: 1.5rem;
    }
    
    .training-section h3 {
        color: white !important;
        margin-bottom: 1rem;
        font-size: 1.1rem;
    }
    
    /* Random State input with +/- buttons */
    .random-state-container {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        margin-top: 0.5rem;
    }
    
    .random-state-input {
        background-color: rgba(139, 92, 246, 0.3);
        border: 1px solid #8b5cf6;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        color: white;
        width: 100px;
        text-align: center;
    }
    
    .random-state-btn {
        background-color: #8b5cf6;
        color: white;
        border: none;
        border-radius: 6px;
        width: 40px;
        height: 40px;
        cursor: pointer;
        font-size: 1.2rem;
        display: flex;
        align-items: center;
        justify-content: center;
        transition: all 0.3s;
    }
    
    .random-state-btn:hover {
        background-color: #7c3aed;
    }
    
    /* Slider styling */
    .stSlider {
        margin-top: 0.5rem;
    }
    
    /* Hide Streamlit default elements (jangan sembunyikan header agar tombol sidebar tetap muncul) */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = 'Dataset'
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

# Sidebar Navigation
with st.sidebar:
    st.markdown('<div class="logo">🌲 ForestCal</div>', unsafe_allow_html=True)
    
    st.markdown("### Menu Utama")
    
    # Menu items
    menu_items = {
        'Dataset': '📊',
        'Preprocessing': '⚙️',
        'Training Data': '📈',
        'Visualisasi Data': '📉'
    }
    
    for menu_name, icon in menu_items.items():
        is_active = st.session_state.page == menu_name
        button_type = "primary" if is_active else "secondary"
        if st.button(f"{icon} {menu_name}", key=f"menu_{menu_name}", use_container_width=True, type=button_type):
            st.session_state.page = menu_name
            st.rerun()
    
    st.markdown("---")
    st.markdown("### Analisis Data Pribadi")
    
    is_personal_active = st.session_state.page == 'Analisis Pribadi'
    personal_button_type = "primary" if is_personal_active else "secondary"
    if st.button("➕ Analisis", key="menu_analisis_pribadi", use_container_width=True, type=personal_button_type):
        st.session_state.page = 'Analisis Pribadi'
        st.rerun()

# Main Content Area
st.markdown('<div class="main-content">', unsafe_allow_html=True)

# Page: Dataset
if st.session_state.page == 'Dataset':
    st.title("Analisis dan Prediksi Pembakaran Kalori Berdasarkan Aktivitas Fisik Menggunakan Data Akuisisi")
    
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
        
        if uploaded_file is not None:
            try:
                # Check file size (200MB limit)
                if uploaded_file.size > 200 * 1024 * 1024:
                    st.error("File terlalu besar! Maksimal 200MB")
                else:
                    st.session_state.df = pd.read_csv(uploaded_file)
                    st.success(f"✅ Dataset berhasil di-upload! ({uploaded_file.size / 1024:.2f} KB)")
            except Exception as e:
                st.error(f"Gagal membaca file: {e}")
                st.session_state.df = None
        else:
            # Try to load sample dataset
            try:
                st.session_state.df = pd.read_csv("exercise_dataset.csv")
                st.info("📁 Menggunakan dataset contoh: exercise_dataset.csv")
            except:
                pass
    
    with col2:
        st.markdown("### Ketentuan Dataset")
        st.markdown("""
        <div class="info-box">
            <p>📄 CSV Only</p>
        </div>
        <div class="info-box">
            <p>💾 Maximal 200MB</p>
        </div>
        <div class="info-box">
            <p>🔤 UTF-8 recommended</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Eksplorasi Data Awal
    if st.session_state.df is not None:
        st.markdown("### Eksplorasi Data Awal")
        st.dataframe(st.session_state.df.head(10), use_container_width=True)
        
        # Data info
        col_info1, col_info2, col_info3 = st.columns(3)
        with col_info1:
            st.metric("Jumlah Baris", len(st.session_state.df))
        with col_info2:
            st.metric("Jumlah Kolom", len(st.session_state.df.columns))
        with col_info3:
            st.metric("Missing Values", st.session_state.df.isnull().sum().sum())
        
        # Next Step
        st.markdown("### Next Step")
        if st.button("Preprocessing Data", use_container_width=True, type="primary"):
            st.session_state.page = 'Preprocessing'
            st.rerun()
    else:
        st.info("👆 Silakan upload dataset CSV untuk melanjutkan")

# Page: Preprocessing
elif st.session_state.page == 'Preprocessing':
    st.title("Eksplorasi Data")
    
    if st.session_state.df is None:
        st.warning("⚠️ Tidak ada dataset. Silakan upload dataset di halaman Dataset terlebih dahulu.")
        if st.button("Kembali ke Dataset"):
            st.session_state.page = 'Dataset'
            st.rerun()
    else:
        df = st.session_state.df.copy()
        
        # Data Table Preview
        st.markdown('<div class="preprocessing-card">', unsafe_allow_html=True)
        st.markdown("### Data Table")
        st.markdown('<div class="table-preview">', unsafe_allow_html=True)
        st.dataframe(df.head(10), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Informasi Dataset Card
        st.markdown('<div class="preprocessing-card">', unsafe_allow_html=True)
        st.markdown("### Informasi Dataset")
        
        num_rows = len(df)
        num_features = len(df.columns)
        missing_values = df.isnull().sum()
        missing_cols = missing_values[missing_values > 0]
        
        st.markdown(f"**1. Jumlah Baris :** {num_rows}")
        st.markdown(f"**2. Jumlah Fitur :** {num_features}")
        
        if len(missing_cols) > 0:
            st.markdown("**3. Jumlah Missing Value**")
            for col in missing_cols.index:
                st.markdown(f"   > {col} : {missing_cols[col]}")
        else:
            st.markdown("**3. Jumlah Missing Value :** 0 (Tidak ada missing value)")
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Detect columns for later use
        all_columns = df.columns.tolist()
        
        # Suggest common column names for target
        suggest_target = None
        candidates = [c for c in all_columns if 'calor' in c.lower() or 'burn' in c.lower() or 'target' in c.lower()]
        if candidates:
            suggest_target = candidates[0]
        
        # Store target and features in session state if not set
        if st.session_state.target_col is None or st.session_state.target_col not in all_columns:
            st.session_state.target_col = suggest_target if suggest_target else all_columns[0]
        
        if st.session_state.feature_cols is None or not all(f in all_columns for f in st.session_state.feature_cols):
            st.session_state.feature_cols = [c for c in all_columns if c not in [st.session_state.target_col, 'ID']]
        
        # Card: Pemilihan Target dan Fitur
        st.markdown('<div class="preprocessing-card">', unsafe_allow_html=True)
        st.markdown("### Pemilihan Target dan Fitur")
        
        col_tgt, col_feat = st.columns(2)
        with col_tgt:
            selected_target = st.selectbox(
                "Pilih kolom target (nilai yang ingin diprediksi)",
                options=all_columns,
                index=all_columns.index(st.session_state.target_col) if st.session_state.target_col in all_columns else 0,
                key="target_col_select"
            )
            st.session_state.target_col = selected_target
        
        with col_feat:
            possible_features = [c for c in all_columns if c != st.session_state.target_col]
            default_features = [
                c for c in st.session_state.feature_cols
                if c in possible_features
            ]
            if not default_features:
                default_features = [c for c in possible_features if c != 'ID']
            selected_features = st.multiselect(
                "Pilih fitur yang digunakan untuk prediksi",
                options=possible_features,
                default=default_features,
                key="feature_cols_select"
            )
            st.session_state.feature_cols = selected_features
        
        st.markdown(
            "Pastikan kolom target benar-benar **kalori yang terbakar** dan fitur hanya berisi "
            "variabel yang diketahui sebelum aktivitas (tidak ada kebocoran label).",
            unsafe_allow_html=False
        )
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Initialize default values for training
        target_col = st.session_state.target_col
        feature_cols = st.session_state.feature_cols
        train_size = 0.8
        random_state = 42
        n_estimators = 200
        max_depth = None
        min_samples_split = 2
        
        # Penanganan Missing Value Card
        st.markdown('<div class="preprocessing-card">', unsafe_allow_html=True)
        st.markdown("### Penanganan Missing Value")
        missing_strategy = st.selectbox(
            "Strategi missing value:",
            options=['drop rows', 'fill numeric mean', 'fill numeric median', 'fill with constant (0)'],
            key="missing_strategy"
        )
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Data Kategorikal Card
        st.markdown('<div class="preprocessing-card">', unsafe_allow_html=True)
        st.markdown("### Data Kategorikal")
        cat_cols = [c for c in df.columns if df[c].dtype == 'object' or df[c].dtype.name == 'category']
        if cat_cols:
            cat_cols_str = ", ".join(cat_cols)
            st.markdown(f"**{cat_cols_str}**")
        else:
            st.markdown("Tidak ada data kategorikal terdeteksi")
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Standard Scaler Option (outside card, at bottom)
        st.markdown("<br>", unsafe_allow_html=True)
        scaling = st.checkbox(
            "Gunakan StandardScaler untuk fitur numerik (tidak wajib untuk Random Forest)",
            value=False,
            key="scaling_option"
        )
        
        # Note: missing_strategy and scaling are automatically stored in session_state
        # via their widget keys ("missing_strategy" and "scaling_option")
        
        # Next Step button
        st.markdown("---")
        if st.button("Lanjut ke Training Data", use_container_width=True, type="primary"):
            st.session_state.page = 'Training Data'
            st.rerun()

# Page: Training Data
elif st.session_state.page == 'Training Data':
    st.title("Pengaturan Training")
    st.markdown("---")
    
    if st.session_state.df is None:
        st.warning("⚠️ Tidak ada dataset. Silakan upload dataset di halaman Dataset terlebih dahulu.")
        if st.button("Kembali ke Dataset"):
            st.session_state.page = 'Dataset'
            st.rerun()
    else:
        df = st.session_state.df.copy()
        
        # Get settings from session state or set defaults
        if st.session_state.target_col is None:
            all_columns = df.columns.tolist()
            candidates = [c for c in all_columns if 'calor' in c.lower() or 'burn' in c.lower() or 'target' in c.lower()]
            st.session_state.target_col = candidates[0] if candidates else all_columns[0]
            st.session_state.feature_cols = [c for c in all_columns if c not in [st.session_state.target_col, 'ID']]
        
        target_col = st.session_state.target_col
        feature_cols = st.session_state.feature_cols
        # Get values from session_state (automatically stored by widgets with keys)
        missing_strategy = st.session_state.get('missing_strategy', 'drop rows')
        scaling = st.session_state.get('scaling_option', True)
        
        # Section 1: Rasio Data Latih
        st.markdown('<div class="training-section">', unsafe_allow_html=True)
        st.markdown("### Rasio Data Latih")
        train_size = st.slider(
            "Rasio Data Latih",
            min_value=0.5,
            max_value=0.9,
            value=0.65,
            step=0.05,
            key="train_size_slider"
        )
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Section 2: Random State
        st.markdown('<div class="training-section">', unsafe_allow_html=True)
        st.markdown("### Random State")
        
        # Initialize random_state in session state if not exists
        if 'random_state' not in st.session_state:
            st.session_state.random_state = 42
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            col_btn1, col_input, col_btn2 = st.columns([1, 2, 1])
            with col_btn1:
                if st.button("−", key="random_state_dec", use_container_width=True):
                    st.session_state.random_state = max(0, st.session_state.random_state - 1)
                    st.rerun()
            with col_input:
                random_state = st.number_input(
                    "Random State",
                    min_value=0,
                    value=st.session_state.random_state,
                    step=1,
                    key="random_state_input",
                    label_visibility="collapsed"
                )
                st.session_state.random_state = random_state
            with col_btn2:
                if st.button("+", key="random_state_inc", use_container_width=True):
                    st.session_state.random_state += 1
                    st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Section 3: Penanganan Target & Outlier
        st.markdown('<div class="training-section">', unsafe_allow_html=True)
        st.markdown("### Penanganan Target & Outlier")
        
        col_out1, col_out2 = st.columns(2)
        with col_out1:
            target_outlier = st.selectbox(
                "Penanganan outlier pada target kalori",
                options=[
                    'Tidak ada',
                    'Trim (buang di luar 1% - 99%)',
                    'Clip (batasi ke 1% - 99%)'
                ],
                key="target_outlier"
            )
        with col_out2:
            log_target = st.checkbox(
                "Gunakan transformasi log pada target (log1p)",
                value=False,
                key="log_target"
            )
        st.markdown(
            "Transformasi log cocok bila distribusi kalori sangat miring (banyak nilai kecil, sedikit yang sangat besar). "
            "Outlier ekstrem dapat dibuang (trim) atau dibatasi (clip) agar error tidak didominasi beberapa titik ekstrem.",
            unsafe_allow_html=False
        )
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Section 4: Hyperparameter Random Forest
        st.markdown('<div class="training-section">', unsafe_allow_html=True)
        st.markdown("### Hyperparameter Random Forest")
        
        n_estimators = st.slider(
            "n_estimators",
            min_value=50,
            max_value=1000,
            value=200,
            step=10,
            key="n_estimators_slider"
        )
        
        max_depth = st.slider(
            "max_depth (None = 0)",
            min_value=0,
            max_value=50,
            value=0,
            step=1,
            key="max_depth_slider"
        )
        if max_depth == 0:
            max_depth = None
        
        min_samples_split = st.slider(
            "min_samples_split",
            min_value=2,
            max_value=10,
            value=2,
            step=1,
            key="min_samples_split_slider"
        )
        
        min_samples_leaf = st.slider(
            "min_samples_leaf",
            min_value=1,
            max_value=20,
            value=1,
            step=1,
            key="min_samples_leaf_slider"
        )
        st.markdown('</div>', unsafe_allow_html=True)
        
        # preprocessing & training
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Jalankan Preprocessing dan Latih Model", use_container_width=True, type="primary"):
            # Validate required variables
            if target_col is None:
                st.error("❌ Kolom target belum dipilih. Silakan kembali ke halaman Preprocessing untuk memilih kolom target.")
                st.stop()
            
            if feature_cols is None or len(feature_cols) == 0:
                st.error("❌ Fitur belum dipilih. Silakan kembali ke halaman Preprocessing untuk memilih fitur.")
                st.stop()
            
            if target_col not in df.columns:
                st.error(f"❌ Kolom target '{target_col}' tidak ditemukan dalam dataset.")
                st.stop()
            
            # Check if all feature columns exist
            missing_features = [f for f in feature_cols if f not in df.columns]
            if missing_features:
                st.error(f"❌ Fitur berikut tidak ditemukan dalam dataset: {', '.join(missing_features)}")
                st.stop()
            
            try:
                df_proc = df.copy()
                
                # Missing handling
                if missing_strategy == 'drop rows':
                    df_proc = df_proc.dropna(subset=feature_cols + [target_col])
                elif missing_strategy == 'fill numeric mean':
                    for c in feature_cols:
                        if np.issubdtype(df_proc[c].dtype, np.number):
                            df_proc[c] = df_proc[c].fillna(df_proc[c].mean())
                        else:
                            df_proc[c] = df_proc[c].fillna(df_proc[c].mode().iloc[0] if len(df_proc[c].mode()) > 0 else 'unknown')
                    df_proc[target_col] = df_proc[target_col].fillna(df_proc[target_col].mean())
                elif missing_strategy == 'fill numeric median':
                    for c in feature_cols:
                        if np.issubdtype(df_proc[c].dtype, np.number):
                            df_proc[c] = df_proc[c].fillna(df_proc[c].median())
                        else:
                            df_proc[c] = df_proc[c].fillna(df_proc[c].mode().iloc[0] if len(df_proc[c].mode()) > 0 else 'unknown')
                    df_proc[target_col] = df_proc[target_col].fillna(df_proc[target_col].median())
                else:
                    df_proc = df_proc.fillna(0)
                
                # Ensure numeric target
                df_proc[target_col] = pd.to_numeric(df_proc[target_col], errors='coerce')
                df_proc = df_proc.dropna(subset=[target_col])
                
                # Target series (original scale)
                y_raw = df_proc[target_col].copy()
                
                # Penanganan outlier pada target
                target_outlier = st.session_state.get('target_outlier', 'Tidak ada')
                if target_outlier in ['Trim (buang di luar 1% - 99%)', 'Clip (batasi ke 1% - 99%)']:
                    q_low = y_raw.quantile(0.01)
                    q_high = y_raw.quantile(0.99)
                    
                    if target_outlier.startswith('Trim'):
                        mask = (y_raw >= q_low) & (y_raw <= q_high)
                        df_proc = df_proc[mask]
                        y_raw = y_raw[mask]
                    else:
                        y_raw = y_raw.clip(q_low, q_high)
                        df_proc[target_col] = y_raw
                
                # Fitur setelah penanganan outlier
                X = df_proc[feature_cols].copy()
                
                # Identify numeric and categorical
                numeric_features = X.select_dtypes(include=[np.number]).columns.tolist()
                categorical_features = X.select_dtypes(include=['object', 'category']).columns.tolist()
                
                # Column transformer
                transformers = []
                if categorical_features:
                    transformers.append(("cat", OneHotEncoder(handle_unknown='ignore', sparse_output=False), categorical_features))
                if numeric_features and scaling:
                    transformers.append(("num", StandardScaler(), numeric_features))
                
                if transformers:
                    preprocessor = ColumnTransformer(transformers=transformers, remainder='passthrough')
                else:
                    preprocessor = 'passthrough'
                
                # Build pipeline
                model = RandomForestRegressor(
                    n_estimators=n_estimators,
                    max_depth=max_depth,
                    min_samples_split=min_samples_split,
                    min_samples_leaf=min_samples_leaf,
                    random_state=random_state
                )
                pipeline = Pipeline(steps=[('preprocessor', preprocessor), ('model', model)])
                
                # Target transform (log1p jika dipilih dan memungkinkan)
                use_log_target = False
                y_for_model = y_raw.copy()
                if st.session_state.get('log_target', False):
                    if (y_raw <= 0).any():
                        st.warning("Transformasi log pada target diabaikan karena terdapat nilai kalori ≤ 0.")
                    else:
                        y_for_model = np.log1p(y_raw)
                        use_log_target = True
                
                # Split data
                if use_log_target:
                    X_train, X_test, y_train, y_test_log, y_train_raw, y_test_raw = train_test_split(
                        X, y_for_model, y_raw, train_size=train_size, random_state=random_state
                    )
                else:
                    X_train, X_test, y_train_raw, y_test_raw = train_test_split(
                        X, y_raw, train_size=train_size, random_state=random_state
                    )
                    y_train = y_train_raw  # untuk keseragaman variabel
                
                # Fit
                with st.spinner('Melatih model...'):
                    pipeline.fit(X_train, y_train)
                
                # Predict di ruang model
                if use_log_target:
                    y_pred_log = pipeline.predict(X_test)
                    y_pred = np.expm1(y_pred_log)
                else:
                    y_pred = pipeline.predict(X_test)
                
                # Baseline model: selalu memprediksi rata-rata y_train (skala asli)
                baseline_pred = np.full_like(y_test_raw, y_train_raw.mean(), dtype=float)
                
                # Store in session state
                st.session_state.df_processed = df_proc
                st.session_state.pipeline = pipeline
                st.session_state.X_test = X_test
                st.session_state.y_test = y_test_raw
                st.session_state.y_pred = y_pred
                st.session_state.X_train = X_train
                st.session_state.y_train = y_train_raw
                st.session_state.y_pred_baseline = baseline_pred
                st.session_state.numeric_features = numeric_features
                st.session_state.categorical_features = categorical_features
                st.session_state.log_target_used = use_log_target
                
                st.success('✅ Pelatihan selesai! Model siap digunakan.')
                
                # Show metrics (di skala asli)
                mae = mean_absolute_error(y_test_raw, y_pred)
                mse = mean_squared_error(y_test_raw, y_pred)
                rmse = np.sqrt(mse)
                r2 = r2_score(y_test_raw, y_pred)
                mape = np.mean(np.abs((y_test_raw - y_pred) / y_test_raw)) * 100 if np.all(y_test_raw != 0) else np.nan
                
                # Baseline metrics
                mae_base = mean_absolute_error(y_test_raw, baseline_pred)
                rmse_base = np.sqrt(mean_squared_error(y_test_raw, baseline_pred))
                r2_base = r2_score(y_test_raw, baseline_pred)
                
                st.markdown("### Hasil Evaluasi Model (Test Set)")
                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    st.metric("MAE (model)", f"{mae:.3f}", delta=f"{(mae_base - mae):.3f} vs baseline")
                with col2:
                    st.metric("RMSE (model)", f"{rmse:.3f}", delta=f"{(rmse_base - rmse):.3f} vs baseline")
                with col3:
                    st.metric("R² (model)", f"{r2:.3f}", delta=f"{(r2 - r2_base):.3f} vs baseline")
                with col4:
                    if not np.isnan(mape):
                        st.metric("MAPE", f"{mape:.2f}%")
                    else:
                        st.metric("MAPE", "NA")
                
                st.info(
                    "Model Random Forest yang baik seharusnya **lebih baik dari baseline rata-rata**. "
                    "Perhatikan delta pada MAE/RMSE/R² untuk menilai apakah model sudah cukup baik."
                )
                
            except Exception as e:
                st.error(f"❌ Terjadi error saat melakukan preprocessing dan training: {str(e)}")
                st.error("Detail error:")
                import traceback
                st.code(traceback.format_exc())
                st.info("💡 Tips: Pastikan dataset sudah di-upload dan kolom target serta fitur sudah dipilih dengan benar.")

# Page: Visualisasi Data
elif st.session_state.page == 'Visualisasi Data':
    st.title("Visualisasi Data")
    
    if st.session_state.pipeline is None:
        st.warning("⚠️ Model belum dilatih. Silakan lakukan preprocessing dan training di halaman Preprocessing terlebih dahulu.")
        if st.button("Kembali ke Preprocessing"):
            st.session_state.page = 'Preprocessing'
            st.rerun()
    else:
        pipeline = st.session_state.pipeline
        y_test = st.session_state.y_test
        y_pred = st.session_state.y_pred
        df_proc = st.session_state.df_processed
        
        # Predicted vs Actual
        st.markdown("### Visualisasi Prediksi vs Aktual")
        fig1, ax1 = plt.subplots(figsize=(8, 6))
        sns.scatterplot(x=y_test, y=y_pred, ax=ax1, color='#8b5cf6', alpha=0.6)
        ax1.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
        ax1.set_xlabel('Actual Calories', color='white')
        ax1.set_ylabel('Predicted Calories', color='white')
        ax1.set_title('Predicted vs Actual', color='white')
        ax1.tick_params(colors='white')
        ax1.spines['bottom'].set_color('white')
        ax1.spines['top'].set_color('white')
        ax1.spines['right'].set_color('white')
        ax1.spines['left'].set_color('white')
        plt.tight_layout()
        st.pyplot(fig1)
        
        # Distribution of residuals
        st.markdown("### Distribusi Residual")
        resid = y_test - y_pred
        fig2, ax2 = plt.subplots(figsize=(8, 6))
        sns.histplot(resid, kde=True, ax=ax2, color='#8b5cf6')
        ax2.set_title('Distribusi Residual (Actual - Predicted)', color='white')
        ax2.set_xlabel('Residual', color='white')
        ax2.set_ylabel('Frequency', color='white')
        ax2.tick_params(colors='white')
        ax2.spines['bottom'].set_color('white')
        ax2.spines['top'].set_color('white')
        ax2.spines['right'].set_color('white')
        ax2.spines['left'].set_color('white')
        plt.tight_layout()
        st.pyplot(fig2)
        
        # Correlation heatmap
        st.markdown("### Heatmap Korelasi (Fitur Numerik)")
        numeric_df = df_proc.select_dtypes(include=[np.number])
        if len(numeric_df.columns) > 1:
            fig3, ax3 = plt.subplots(figsize=(10, 8))
            sns.heatmap(numeric_df.corr(), annot=True, fmt='.2f', ax=ax3, cmap='viridis')
            ax3.set_title('Correlation Heatmap', color='white')
            plt.tight_layout()
            st.pyplot(fig3)

# Page: Analisis Pribadi
elif st.session_state.page == 'Analisis Pribadi':
    st.title("Analisis Data Pribadi")
    
    if st.session_state.pipeline is None:
        st.warning("⚠️ Model belum dilatih. Silakan lakukan preprocessing dan training di halaman Preprocessing terlebih dahulu.")
        if st.button("Kembali ke Preprocessing"):
            st.session_state.page = 'Preprocessing'
            st.rerun()
    else:
        pipeline = st.session_state.pipeline
        df_proc = st.session_state.df_processed
        feature_cols = st.session_state.feature_cols
        numeric_features = st.session_state.numeric_features
        categorical_features = st.session_state.categorical_features
        log_target_used = st.session_state.get('log_target_used', False)
        
        st.markdown("### Prediksi Interaktif")
        st.write("Masukkan nilai fitur untuk memprediksi pembakaran kalori:")
        
        sample_input = {}
        
        # Create input fields
        cols = st.columns(2)
        col_idx = 0
        for c in feature_cols:
            with cols[col_idx % 2]:
                if c in numeric_features:
                    val = st.number_input(
                        f"{c}",
                        value=float(df_proc[c].median()),
                        min_value=float(df_proc[c].min()) if df_proc[c].min() != np.inf else None,
                        max_value=float(df_proc[c].max()) if df_proc[c].max() != np.inf else None,
                        step=0.1
                    )
                    sample_input[c] = val
                else:
                    vals = df_proc[c].unique().tolist()
                    sel = st.selectbox(f"{c}", options=vals, index=0)
                    sample_input[c] = sel
            col_idx += 1
        
        if st.button('Prediksi Pembakaran Kalori', use_container_width=True, type="primary"):
            try:
                sample_df = pd.DataFrame([sample_input])
                pred_val_raw = pipeline.predict(sample_df)[0]
                pred_val = np.expm1(pred_val_raw) if log_target_used else pred_val_raw
                st.success(f"🔥 **Perkiraan pembakaran kalori: {pred_val:.2f} kalori**")
                
                # Show prediction with confidence interval (using std from residuals)
                if hasattr(st.session_state, 'y_test'):
                    resid = st.session_state.y_test - st.session_state.y_pred
                    std_resid = resid.std()
                    st.info(f"📊 Rentang prediksi (95% confidence): {pred_val - 1.96*std_resid:.2f} - {pred_val + 1.96*std_resid:.2f} kalori")
            except Exception as e:
                st.error(f"Gagal melakukan prediksi: {e}")
        
        # Download predictions
        st.markdown("---")
        st.markdown("### Download Hasil Prediksi (Test Set)")
        if hasattr(st.session_state, 'X_test'):
            out_df = st.session_state.X_test.copy()
            out_df['actual'] = st.session_state.y_test
            out_df['predicted'] = st.session_state.y_pred
            csv = out_df.to_csv(index=False)
            b64 = base64.b64encode(csv.encode()).decode()
            href = f'<a href="data:file/csv;base64,{b64}" download="predictions.csv" style="background-color: #8b5cf6; color: white; padding: 0.5rem 1.5rem; border-radius: 8px; text-decoration: none; display: inline-block;">📥 Download predictions.csv</a>'
            st.markdown(href, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.caption('🌲 ForestCal - Aplikasi Analisis dan Prediksi Pembakaran Kalori | Dikembangkan untuk tugas mata kuliah')
