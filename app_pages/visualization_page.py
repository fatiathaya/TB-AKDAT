"""
Visualization page for ForestCal application
"""
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from utils.session_manager import navigate_to
from ml_models.training import get_feature_importance, plot_feature_importance


def render_visualization_page():
    """Render the Visualization page"""
    st.title("Visualisasi Data")
    
    if st.session_state.pipeline is None:
        st.warning("⚠️ Model belum dilatih. Silakan lakukan preprocessing dan training di halaman Preprocessing terlebih dahulu.")
        if st.button("Kembali ke Preprocessing"):
            navigate_to('Preprocessing')
        return
    
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
    numeric_df = df_proc.select_dtypes(include=['number'])
    if len(numeric_df.columns) > 1:
        fig3, ax3 = plt.subplots(figsize=(10, 8))
        sns.heatmap(numeric_df.corr(), annot=True, fmt='.2f', ax=ax3, cmap='viridis')
        ax3.set_title('Correlation Heatmap', color='white')
        plt.tight_layout()
        st.pyplot(fig3)
    
    # Feature Importance
    st.markdown("---")
    st.markdown("### Analisis Feature Importance")
    
    # Generate feature importance if not already in session state
    if not hasattr(st.session_state, 'feature_importances') or st.session_state.feature_importances is None:
        importance_df = get_feature_importance(pipeline)
        if importance_df is not None:
            st.session_state.feature_importances = importance_df
    
    # Display feature importance chart and table
    if hasattr(st.session_state, 'feature_importances') and st.session_state.feature_importances is not None:
        importance_df = st.session_state.feature_importances
        
        # Chart
        fig = plot_feature_importance(importance_df, top_n=15)
        if fig is not None:
            st.pyplot(fig)
        
        # Table
        st.markdown("**Daftar Feature Importance (Top 15)**")
        st.dataframe(importance_df.head(15), use_container_width=True)
    else:
        st.warning("⚠️ Feature importance tidak tersedia. Silakan lakukan training ulang.")

