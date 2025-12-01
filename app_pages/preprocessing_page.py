"""
Preprocessing page for ForestCal application
"""
import streamlit as st
from config.settings import MISSING_STRATEGIES, EXCLUDE_COLUMNS
from utils.data_handler import (
    suggest_target_column,
    suggest_feature_columns,
    get_categorical_columns
)
from utils.session_manager import navigate_to


def render_preprocessing_page():
    """Render the Preprocessing page"""
    st.title("Eksplorasi Data")
    
    if st.session_state.df is None:
        st.warning("⚠️ Tidak ada dataset. Silakan upload dataset di halaman Dataset terlebih dahulu.")
        if st.button("Kembali ke Dataset"):
            navigate_to('Dataset')
        return
    
    df = st.session_state.df.copy()
    
    # Data Table Preview
    st.markdown('<div class="preprocessing-card">', unsafe_allow_html=True)
    st.markdown("### Data Table")
    st.dataframe(df.head(10), use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Get column info
    all_columns = df.columns.tolist()
    
    # Suggest target column
    if st.session_state.target_col is None or st.session_state.target_col not in all_columns:
        st.session_state.target_col = suggest_target_column(all_columns)
        if st.session_state.target_col is None:
            st.session_state.target_col = all_columns[0]
    
    # Suggest features
    if st.session_state.feature_cols is None or not all(f in all_columns for f in st.session_state.feature_cols):
        st.session_state.feature_cols = suggest_feature_columns(
            all_columns,
            st.session_state.target_col,
            EXCLUDE_COLUMNS
        )
    
    # Card: Pemilihan Target dan Fitur
    st.markdown('<div class="preprocessing-card">', unsafe_allow_html=True)
    st.markdown("### Pemilihan Target dan Fitur")
    
    # Target Selection
    selected_target = st.selectbox(
        "Pilih kolom target (nilai yang ingin diprediksi)",
        options=all_columns,
        index=all_columns.index(st.session_state.target_col) if st.session_state.target_col in all_columns else 0,
        key="target_col_select"
    )
    st.session_state.target_col = selected_target
    
    # Feature Selection
    possible_features = [c for c in all_columns if c != st.session_state.target_col]
    default_features = [
        c for c in st.session_state.feature_cols
        if c in possible_features
    ]
    if not default_features:
        default_features = [c for c in possible_features if c not in EXCLUDE_COLUMNS]
    
    selected_features = st.multiselect(
        "Pilih fitur yang digunakan untuk prediksi",
        options=possible_features,
        default=default_features,
        key="feature_cols_select"
    )
    st.session_state.feature_cols = selected_features
    
    # Info note
    st.markdown(
        '<div class="info-note"><strong>Catatan:</strong> Pastikan kolom target benar-benar <strong>kalori yang terbakar</strong> dan fitur hanya berisi variabel yang diketahui sebelum aktivitas (tidak ada kebocoran label).</div>',
        unsafe_allow_html=True
    )
    
    # Warning jika fitur penting tidak dipilih
    critical_features = []
    if 'Actual Weight' in all_columns and 'Actual Weight' not in st.session_state.feature_cols:
        critical_features.append('Actual Weight')
    if 'Gender' in all_columns and 'Gender' not in st.session_state.feature_cols:
        critical_features.append('Gender')
    
    if critical_features:
        st.warning(
            f"⚠️ **FITUR PENTING BELUM DIPILIH**: {', '.join(critical_features)}\n\n"
            f"Fitur ini sangat berpengaruh pada akurasi prediksi kalori! "
            f"Tambahkan ke fitur untuk meningkatkan R² secara signifikan."
        )
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Penanganan Missing Value Card
    st.markdown('<div class="preprocessing-card">', unsafe_allow_html=True)
    st.markdown("### Penanganan Missing Value")
    missing_strategy = st.selectbox(
        "Strategi missing value:",
        options=MISSING_STRATEGIES,
        key="missing_strategy"
    )
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Data Kategorikal Card
    st.markdown('<div class="preprocessing-card">', unsafe_allow_html=True)
    st.markdown("### Data Kategorikal")
    cat_cols = get_categorical_columns(df)
    if cat_cols:
        cat_cols_str = ", ".join(cat_cols)
        st.markdown(f"**{cat_cols_str}**")
    else:
        st.markdown("Tidak ada data kategorikal terdeteksi")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Standard Scaler Option
    st.markdown("<br>", unsafe_allow_html=True)
    scaling = st.checkbox(
        "Gunakan StandardScaler untuk fitur numerik (tidak wajib untuk Random Forest)",
        value=False,
        key="scaling_option"
    )
    
    # Next Step button
    st.markdown("---")
    if st.button("Lanjut ke Training Data", use_container_width=True, type="primary"):
        navigate_to('Training Data')

