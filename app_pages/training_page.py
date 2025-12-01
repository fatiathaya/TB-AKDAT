"""
Training page for ForestCal application
"""
import streamlit as st
from config.settings import (
    DEFAULT_TRAIN_SIZE,
    DEFAULT_N_ESTIMATORS,
    DEFAULT_MAX_DEPTH,
    DEFAULT_MIN_SAMPLES_SPLIT,
    DEFAULT_MIN_SAMPLES_LEAF
)
from ml_models.preprocessing import preprocess_data
from ml_models.training import train_model, evaluate_model, get_feature_importance
from utils.session_manager import navigate_to


def render_training_page():
    """Render the Training page"""
    st.title("Pengaturan Training")
    
    if st.session_state.df is None:
        st.warning("⚠️ Tidak ada dataset. Silakan upload dataset di halaman Dataset terlebih dahulu.")
        if st.button("Kembali ke Dataset"):
            navigate_to('Dataset')
        return
    
    df = st.session_state.df.copy()
    
    # Get settings from session state
    if st.session_state.target_col is None:
        st.error("❌ Kolom target belum dipilih. Silakan kembali ke halaman Preprocessing.")
        if st.button("Kembali ke Preprocessing"):
            navigate_to('Preprocessing')
        return
    
    target_col = st.session_state.target_col
    feature_cols = st.session_state.feature_cols
    missing_strategy = st.session_state.get('missing_strategy', 'drop rows')
    scaling = st.session_state.get('scaling_option', False)
    
    # Section 1: Rasio Data Latih
    st.markdown('<div class="training-section">', unsafe_allow_html=True)
    st.markdown("### Rasio Data Latih")
    train_size = st.slider(
        "Rasio Data Latih",
        min_value=0.5,
        max_value=0.9,
        value=DEFAULT_TRAIN_SIZE,
        step=0.05,
        key="train_size_slider"
    )
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Section 2: Random State
    st.markdown('<div class="training-section">', unsafe_allow_html=True)
    st.markdown("### Random State")
    
    random_state = st.slider(
        "Random State (seed untuk reprodusibilitas hasil)",
        min_value=0,
        max_value=100,
        value=st.session_state.random_state,
        step=1,
        key="random_state_slider",
        help="Random state untuk reproducibility. Gunakan nilai yang sama untuk hasil yang konsisten."
    )
    st.session_state.random_state = random_state
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Section 3: Hyperparameter Random Forest
    st.markdown('<div class="training-section">', unsafe_allow_html=True)
    st.markdown("### Hyperparameter Random Forest")
    
    n_estimators = st.slider(
        "n_estimators (lebih banyak = lebih stabil)",
        min_value=100,
        max_value=1000,
        value=DEFAULT_N_ESTIMATORS,
        step=50,
        key="n_estimators_slider",
        help="Jumlah pohon. Nilai tinggi (500-1000) biasanya lebih baik tapi lebih lambat."
    )
    
    max_depth = st.slider(
        "max_depth (None = 0, batasi untuk mengurangi overfitting)",
        min_value=0,
        max_value=50,
        value=DEFAULT_MAX_DEPTH,
        step=1,
        key="max_depth_slider",
        help="Kedalaman maksimal pohon. None = unlimited (bisa overfit). 10-30 biasanya baik."
    )
    if max_depth == 0:
        max_depth = None
    
    min_samples_split = st.slider(
        "min_samples_split (min sampel untuk split)",
        min_value=2,
        max_value=20,
        value=DEFAULT_MIN_SAMPLES_SPLIT,
        step=1,
        key="min_samples_split_slider",
        help="Minimal sampel untuk membagi node. Nilai lebih besar = lebih konservatif."
    )
    
    min_samples_leaf = st.slider(
        "min_samples_leaf (min sampel per leaf)",
        min_value=1,
        max_value=20,
        value=DEFAULT_MIN_SAMPLES_LEAF,
        step=1,
        key="min_samples_leaf_slider",
        help="Minimal sampel di setiap leaf. Nilai lebih besar = prediksi lebih halus."
    )
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Training button
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Jalankan Preprocessing dan Latih Model", use_container_width=True, type="primary"):
        # Validate
        if not feature_cols or len(feature_cols) == 0:
            st.error("❌ Fitur belum dipilih. Silakan kembali ke halaman Preprocessing untuk memilih fitur.")
            return
        
        if target_col not in df.columns:
            st.error(f"❌ Kolom target '{target_col}' tidak ditemukan dalam dataset.")
            return
        
        missing_features = [f for f in feature_cols if f not in df.columns]
        if missing_features:
            st.error(f"❌ Fitur berikut tidak ditemukan dalam dataset: {', '.join(missing_features)}")
            return
        
        try:
            # Preprocessing
            with st.spinner('Memproses data...'):
                preprocess_result = preprocess_data(
                    df, feature_cols, target_col, missing_strategy, scaling
                )
            
            X = preprocess_result['X']
            y = preprocess_result['y']
            df_proc = preprocess_result['df_processed']
            preprocessor = preprocess_result['preprocessor']
            numeric_features = preprocess_result['numeric_features']
            categorical_features = preprocess_result['categorical_features']
            
            # Training
            with st.spinner('Melatih model...'):
                train_result = train_model(
                    X, y, preprocessor, train_size, random_state,
                    n_estimators, max_depth, min_samples_split, min_samples_leaf
                )
            
            pipeline = train_result['pipeline']
            X_train = train_result['X_train']
            X_test = train_result['X_test']
            y_train = train_result['y_train']
            y_test = train_result['y_test']
            y_pred = train_result['y_pred']
            y_pred_baseline = train_result['y_pred_baseline']
            
            # Evaluation
            metrics = evaluate_model(y_test, y_pred, y_pred_baseline)
            
            # Store in session state
            st.session_state.df_processed = df_proc
            st.session_state.pipeline = pipeline
            st.session_state.X_test = X_test
            st.session_state.y_test = y_test
            st.session_state.y_pred = y_pred
            st.session_state.X_train = X_train
            st.session_state.y_train = y_train
            st.session_state.y_pred_baseline = y_pred_baseline
            st.session_state.numeric_features = numeric_features
            st.session_state.categorical_features = categorical_features
            st.session_state.original_feature_cols = feature_cols
            
            st.success('✅ Pelatihan selesai! Model siap digunakan.')
            
            # Display metrics
            st.markdown("### Hasil Evaluasi Model (Test Set)")
            
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("MAE (model)", f"{metrics['mae']:.3f}", 
                         delta=f"{metrics['mae_delta']:.3f} vs baseline")
            with col2:
                st.metric("RMSE (model)", f"{metrics['rmse']:.3f}", 
                         delta=f"{metrics['rmse_delta']:.3f} vs baseline")
            with col3:
                st.metric("R² (model)", f"{metrics['r2']:.3f}", 
                         delta=f"{metrics['r2_delta']:.3f} vs baseline")
            with col4:
                if not pd.isna(metrics['mape']):
                    st.metric("MAPE", f"{metrics['mape']:.2f}%")
                else:
                    st.metric("MAPE", "NA")
            
            st.info(
                "Model Random Forest yang baik seharusnya **lebih baik dari baseline rata-rata**. "
                "Perhatikan delta pada MAE/RMSE/R² untuk menilai apakah model sudah cukup baik."
            )
            
            # Generate and store feature importance for visualization page
            importance_df = get_feature_importance(pipeline)
            if importance_df is not None:
                st.session_state.feature_importances = importance_df
            
        except Exception as e:
            st.error(f"❌ Terjadi error saat melakukan preprocessing dan training: {str(e)}")
            st.error("Detail error:")
            import traceback
            st.code(traceback.format_exc())
            st.info("💡 Tips: Pastikan dataset sudah di-upload dan kolom target serta fitur sudah dipilih dengan benar.")


# Import pandas for isna check
import pandas as pd

