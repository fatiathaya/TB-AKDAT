"""
Data handling utilities for ForestCal application
"""
import pandas as pd
import streamlit as st
from config.settings import MAX_FILE_SIZE_MB


def load_dataset(uploaded_file):
    """
    Load dataset from uploaded file or use default
    
    Args:
        uploaded_file: Streamlit UploadedFile object
        
    Returns:
        tuple: (dataframe, message, message_type)
    """
    if uploaded_file is not None:
        try:
            # Check file size
            file_size_mb = uploaded_file.size / (1024 * 1024)
            if file_size_mb > MAX_FILE_SIZE_MB:
                return None, f"File terlalu besar! Maksimal {MAX_FILE_SIZE_MB}MB", "error"
            
            df = pd.read_csv(uploaded_file)
            message = f"✅ Dataset berhasil di-upload! ({uploaded_file.size / 1024:.2f} KB)"
            return df, message, "success"
            
        except Exception as e:
            return None, f"Gagal membaca file: {e}", "error"
    else:
        # Try to load sample dataset
        try:
            df = pd.read_csv("exercise_dataset.csv")
            message = "📁 Menggunakan dataset contoh: exercise_dataset.csv"
            return df, message, "info"
        except:
            return None, None, None


def validate_dataset(df):
    """
    Validate basic properties of the dataset
    
    Args:
        df: pandas DataFrame
        
    Returns:
        dict: Dataset statistics
    """
    if df is None:
        return None
    
    return {
        'n_rows': len(df),
        'n_cols': len(df.columns),
        'n_missing': df.isnull().sum().sum(),
        'columns': df.columns.tolist(),
        'dtypes': df.dtypes.to_dict()
    }


def suggest_target_column(columns):
    """
    Suggest target column based on column names
    
    Args:
        columns: list of column names
        
    Returns:
        str: suggested column name or None
    """
    target_keywords = ['calor', 'burn', 'target']
    candidates = [
        c for c in columns
        if any(kw in c.lower() for kw in target_keywords)
    ]
    return candidates[0] if candidates else None


def suggest_feature_columns(all_columns, target_col, exclude_cols):
    """
    Suggest feature columns based on priority
    
    Args:
        all_columns: list of all column names
        target_col: target column name
        exclude_cols: list of columns to exclude
        
    Returns:
        list: suggested feature columns in priority order
    """
    from config.settings import (
        PRIORITY_WEIGHT_FEATURES,
        PRIORITY_DEMOGRAPHIC,
        PRIORITY_EXERCISE,
        PRIORITY_ENVIRONMENTAL
    )
    
    important_features = []
    
    # Priority 1: Weight features
    weight_candidates = [
        c for c in all_columns
        if any(kw in c.lower() for kw in PRIORITY_WEIGHT_FEATURES)
    ]
    important_features.extend(weight_candidates)
    
    # Priority 2: Demographic features
    for feat in PRIORITY_DEMOGRAPHIC:
        if feat in all_columns and feat not in important_features:
            important_features.append(feat)
    
    # Priority 3: Exercise features
    for feat in PRIORITY_EXERCISE:
        if feat in all_columns and feat not in important_features:
            important_features.append(feat)
    
    # Priority 4: Environmental features
    for feat in PRIORITY_ENVIRONMENTAL:
        if feat in all_columns and feat not in important_features:
            important_features.append(feat)
    
    # Add remaining features
    for col in all_columns:
        if (col not in important_features and 
            col not in exclude_cols and 
            col != target_col):
            important_features.append(col)
    
    return important_features


def get_categorical_columns(df):
    """
    Get list of categorical columns
    
    Args:
        df: pandas DataFrame
        
    Returns:
        list: categorical column names
    """
    return [
        c for c in df.columns
        if df[c].dtype == 'object' or df[c].dtype.name == 'category'
    ]

