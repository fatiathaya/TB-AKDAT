"""
Data preprocessing functions for ForestCal application
"""
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer


def handle_missing_values(df, feature_cols, target_col, strategy='drop rows'):
    """
    Handle missing values in the dataset
    
    Args:
        df: pandas DataFrame
        feature_cols: list of feature column names
        target_col: target column name
        strategy: missing value strategy
        
    Returns:
        pandas DataFrame
    """
    df_proc = df.copy()
    
    if strategy == 'drop rows':
        df_proc = df_proc.dropna(subset=feature_cols + [target_col])
        
    elif strategy == 'fill numeric mean':
        for c in feature_cols:
            if np.issubdtype(df_proc[c].dtype, np.number):
                df_proc[c] = df_proc[c].fillna(df_proc[c].mean())
            else:
                mode_val = df_proc[c].mode()
                df_proc[c] = df_proc[c].fillna(
                    mode_val.iloc[0] if len(mode_val) > 0 else 'unknown'
                )
        df_proc[target_col] = df_proc[target_col].fillna(df_proc[target_col].mean())
        
    elif strategy == 'fill numeric median':
        for c in feature_cols:
            if np.issubdtype(df_proc[c].dtype, np.number):
                df_proc[c] = df_proc[c].fillna(df_proc[c].median())
            else:
                mode_val = df_proc[c].mode()
                df_proc[c] = df_proc[c].fillna(
                    mode_val.iloc[0] if len(mode_val) > 0 else 'unknown'
                )
        df_proc[target_col] = df_proc[target_col].fillna(df_proc[target_col].median())
        
    else:  # fill with constant (0)
        df_proc = df_proc.fillna(0)
    
    return df_proc


def prepare_features_target(df_proc, feature_cols, target_col):
    """
    Prepare features and target from processed dataframe
    
    Args:
        df_proc: processed DataFrame
        feature_cols: list of feature column names
        target_col: target column name
        
    Returns:
        tuple: (X, y, df_proc)
    """
    # Ensure numeric target
    df_proc[target_col] = pd.to_numeric(df_proc[target_col], errors='coerce')
    df_proc = df_proc.dropna(subset=[target_col])
    
    # Split features and target
    y = df_proc[target_col].copy()
    X = df_proc[feature_cols].copy()
    
    return X, y, df_proc


def identify_feature_types(X):
    """
    Identify numeric and categorical features
    
    Args:
        X: features DataFrame
        
    Returns:
        tuple: (numeric_features, categorical_features)
    """
    numeric_features = X.select_dtypes(include=[np.number]).columns.tolist()
    categorical_features = X.select_dtypes(include=['object', 'category']).columns.tolist()
    
    return numeric_features, categorical_features


def create_preprocessor(numeric_features, categorical_features, use_scaling=False):
    """
    Create preprocessing pipeline
    
    Args:
        numeric_features: list of numeric feature names
        categorical_features: list of categorical feature names
        use_scaling: whether to apply StandardScaler
        
    Returns:
        ColumnTransformer or str ('passthrough')
    """
    transformers = []
    
    if categorical_features:
        transformers.append((
            "cat",
            OneHotEncoder(handle_unknown='ignore', sparse_output=False),
            categorical_features
        ))
    
    if numeric_features and use_scaling:
        transformers.append((
            "num",
            StandardScaler(),
            numeric_features
        ))
    
    if transformers:
        return ColumnTransformer(transformers=transformers, remainder='passthrough')
    else:
        return 'passthrough'


def preprocess_data(df, feature_cols, target_col, missing_strategy='drop rows', use_scaling=False):
    """
    Complete preprocessing pipeline
    
    Args:
        df: raw DataFrame
        feature_cols: list of feature column names
        target_col: target column name
        missing_strategy: strategy for handling missing values
        use_scaling: whether to use StandardScaler
        
    Returns:
        dict: {
            'X': features DataFrame,
            'y': target Series,
            'df_processed': processed DataFrame,
            'preprocessor': preprocessing pipeline,
            'numeric_features': list,
            'categorical_features': list
        }
    """
    # Handle missing values
    df_proc = handle_missing_values(df, feature_cols, target_col, missing_strategy)
    
    # Prepare features and target
    X, y, df_proc = prepare_features_target(df_proc, feature_cols, target_col)
    
    # Identify feature types
    numeric_features, categorical_features = identify_feature_types(X)
    
    # Create preprocessor
    preprocessor = create_preprocessor(numeric_features, categorical_features, use_scaling)
    
    return {
        'X': X,
        'y': y,
        'df_processed': df_proc,
        'preprocessor': preprocessor,
        'numeric_features': numeric_features,
        'categorical_features': categorical_features
    }

