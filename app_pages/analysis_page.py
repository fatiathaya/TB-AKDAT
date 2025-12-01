"""
Analysis page for ForestCal application
"""
import streamlit as st
import pandas as pd
import numpy as np
import base64
from utils.session_manager import navigate_to


def render_analysis_page():
    """Render the Personal Analysis page"""
    st.title("Analisis Data Pribadi")
    
    if st.session_state.pipeline is None:
        st.warning("⚠️ Model belum dilatih. Silakan lakukan preprocessing dan training di halaman Preprocessing terlebih dahulu.")
        if st.button("Kembali ke Preprocessing"):
            navigate_to('Preprocessing')
        return
    
    pipeline = st.session_state.pipeline
    df_proc = st.session_state.df_processed
    original_feature_cols = st.session_state.get('original_feature_cols', st.session_state.feature_cols)
    numeric_features = st.session_state.numeric_features
    categorical_features = st.session_state.categorical_features
    
    st.markdown("### Prediksi Interaktif")
    st.write("Masukkan nilai fitur untuk memprediksi pembakaran kalori:")
    
    sample_input = {}
    
    # Create input fields
    cols = st.columns(2)
    col_idx = 0
    for c in original_feature_cols:
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
            pred_val = pipeline.predict(sample_df)[0]
            st.success(f"🔥 **Perkiraan pembakaran kalori: {pred_val:.2f} kalori**")
            
            # Show prediction with confidence interval
            if hasattr(st.session_state, 'y_test'):
                resid = st.session_state.y_test - st.session_state.y_pred
                std_resid = resid.std()
                st.info(f"📊 Rentang prediksi (95% confidence): {pred_val - 1.96*std_resid:.2f} - {pred_val + 1.96*std_resid:.2f} kalori")
            
        except Exception as e:
            st.error(f"Gagal melakukan prediksi: {e}")
            import traceback
            st.code(traceback.format_exc())
    
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

