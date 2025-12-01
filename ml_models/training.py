"""
Model training and evaluation for ForestCal application
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


def train_model(X, y, preprocessor, train_size=0.8, random_state=42, 
                n_estimators=500, max_depth=20, min_samples_split=5, 
                min_samples_leaf=2):
    """
    Train Random Forest model
    
    Args:
        X: features DataFrame
        y: target Series
        preprocessor: preprocessing pipeline
        train_size: proportion of training data
        random_state: random state for reproducibility
        n_estimators: number of trees
        max_depth: maximum depth of trees (None for unlimited)
        min_samples_split: minimum samples required to split
        min_samples_leaf: minimum samples required at leaf node
        
    Returns:
        dict: {
            'pipeline': trained pipeline,
            'X_train': training features,
            'X_test': test features,
            'y_train': training target,
            'y_test': test target,
            'y_pred': predictions on test set,
            'y_pred_baseline': baseline predictions
        }
    """
    # Build Random Forest Regressor
    model = RandomForestRegressor(
        n_estimators=n_estimators,
        max_depth=max_depth,
        min_samples_split=min_samples_split,
        min_samples_leaf=min_samples_leaf,
        max_features='sqrt',
        bootstrap=True,
        oob_score=False,
        n_jobs=-1,
        random_state=random_state
    )
    
    # Create pipeline
    pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('model', model)
    ])
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, train_size=train_size, random_state=random_state
    )
    
    # Train model
    pipeline.fit(X_train, y_train)
    
    # Predict
    y_pred = pipeline.predict(X_test)
    
    # Baseline predictions (always predict mean)
    y_pred_baseline = np.full_like(y_test, y_train.mean(), dtype=float)
    
    return {
        'pipeline': pipeline,
        'X_train': X_train,
        'X_test': X_test,
        'y_train': y_train,
        'y_test': y_test,
        'y_pred': y_pred,
        'y_pred_baseline': y_pred_baseline
    }


def evaluate_model(y_test, y_pred, y_pred_baseline):
    """
    Evaluate model performance
    
    Args:
        y_test: true target values
        y_pred: predicted values
        y_pred_baseline: baseline predictions
        
    Returns:
        dict: evaluation metrics
    """
    # Model metrics
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)
    
    # MAPE (handle division by zero)
    if np.all(y_test != 0):
        mape = np.mean(np.abs((y_test - y_pred) / y_test)) * 100
    else:
        mape = np.nan
    
    # Baseline metrics
    mae_base = mean_absolute_error(y_test, y_pred_baseline)
    rmse_base = np.sqrt(mean_squared_error(y_test, y_pred_baseline))
    r2_base = r2_score(y_test, y_pred_baseline)
    
    return {
        'mae': mae,
        'rmse': rmse,
        'r2': r2,
        'mape': mape,
        'mae_baseline': mae_base,
        'rmse_baseline': rmse_base,
        'r2_baseline': r2_base,
        'mae_delta': mae_base - mae,
        'rmse_delta': rmse_base - rmse,
        'r2_delta': r2 - r2_base
    }


def get_feature_importance(pipeline):
    """
    Extract feature importances from trained pipeline
    
    Args:
        pipeline: trained sklearn Pipeline
        
    Returns:
        pandas DataFrame with features and importances
    """
    try:
        # Get Random Forest model
        rf_model = pipeline.named_steps['model']
        importances = rf_model.feature_importances_
        
        # Get feature names after preprocessing
        if hasattr(pipeline.named_steps['preprocessor'], 'get_feature_names_out'):
            feature_names = pipeline.named_steps['preprocessor'].get_feature_names_out()
        else:
            feature_names = [f"feature_{i}" for i in range(len(importances))]
        
        # Create DataFrame
        importance_df = pd.DataFrame({
            'Feature': feature_names,
            'Importance': importances
        }).sort_values('Importance', ascending=False)
        
        return importance_df
        
    except Exception as e:
        return None


def plot_feature_importance(importance_df, top_n=15):
    """
    Create feature importance plot
    
    Args:
        importance_df: DataFrame with feature importance
        top_n: number of top features to display
        
    Returns:
        matplotlib figure
    """
    if importance_df is None:
        return None
    
    # Get top features
    top_features = importance_df.head(top_n)
    
    # Create plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.barh(top_features['Feature'], top_features['Importance'], color='#8b5cf6')
    ax.set_xlabel('Importance Score', color='white')
    ax.set_title(f'Top {top_n} Feature Importance', color='white')
    ax.tick_params(colors='white')
    ax.spines['bottom'].set_color('white')
    ax.spines['top'].set_color('white')
    ax.spines['right'].set_color('white')
    ax.spines['left'].set_color('white')
    ax.invert_yaxis()
    plt.tight_layout()
    
    return fig

