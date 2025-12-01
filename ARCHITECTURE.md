# Arsitektur ForestCal

## Overview

ForestCal menggunakan arsitektur modular berbasis **Separation of Concerns** untuk memisahkan logika bisnis, presentasi, dan konfigurasi.

## Layer Architecture

```
┌─────────────────────────────────────┐
│   Presentation Layer (UI)           │
│   - streamlit_calorie_app.py        │
│   - app_pages/*.py                   │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│   Business Logic Layer               │
│   - ml_models/*.py                   │
│   - utils/*.py                       │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│   Configuration & Styling Layer     │
│   - config/*.py                      │
│   - styles/*.py                      │
└─────────────────────────────────────┘
```

## Komponen Utama

### 1. Presentation Layer

**Tanggung Jawab**: Menampilkan UI dan menerima input user

- **streamlit_calorie_app.py**: Main orchestrator
  - Setup konfigurasi aplikasi
  - Routing halaman
  - Render sidebar & footer
  
- **app_pages/**: Halaman-halaman aplikasi
  - `dataset_page.py`: Upload & preview data
  - `preprocessing_page.py`: Feature selection & data cleaning
  - `training_page.py`: Model training & hyperparameter tuning
  - `visualization_page.py`: Charts & visualisasi hasil
  - `analysis_page.py`: Prediksi interaktif

### 2. Business Logic Layer

**Tanggung Jawab**: Logika inti aplikasi

- **ml_models/**: Machine Learning logic
  - `preprocessing.py`: Data transformation pipeline
    - Handle missing values
    - Feature encoding
    - Feature scaling
  - `training.py`: Model management
    - Train Random Forest
    - Model evaluation
    - Feature importance calculation

- **utils/**: Helper functions
  - `session_manager.py`: State management
    - Initialize session state
    - Navigate between pages
    - Get/set session values
  - `data_handler.py`: Data utilities
    - Load & validate dataset
    - Suggest target & features
    - Get categorical columns

### 3. Configuration & Styling Layer

**Tanggung Jawab**: Konfigurasi & styling

- **config/**: Application configuration
  - `settings.py`: Constants & defaults
    - Page config
    - Menu items
    - Default hyperparameters
    - Feature priorities

- **styles/**: Visual styling
  - `custom_css.py`: Custom CSS
    - Color schemes
    - Component styling
    - Responsive design

## Data Flow

```
User Input (Upload CSV)
    ↓
data_handler.load_dataset()
    ↓
Session State (st.session_state.df)
    ↓
User selects features/target
    ↓
preprocessing.preprocess_data()
    ↓
training.train_model()
    ↓
training.evaluate_model()
    ↓
Display results & visualizations
    ↓
analysis_page: Interactive prediction
```

## Design Patterns

### 1. **Module Pattern**
Setiap folder adalah modul independen dengan `__init__.py`

### 2. **Facade Pattern**
`streamlit_calorie_app.py` sebagai facade yang menyembunyikan kompleksitas

### 3. **Strategy Pattern**
`preprocessing.py` menggunakan strategy untuk handle missing values

### 4. **Pipeline Pattern**
`training.py` menggunakan sklearn Pipeline untuk preprocessing & training

## Session State Management

```python
st.session_state = {
    'page': str,                    # Current page
    'df': DataFrame,                # Raw dataset
    'df_processed': DataFrame,      # Processed dataset
    'pipeline': Pipeline,           # Trained model
    'target_col': str,             # Target column name
    'feature_cols': list,          # Feature columns
    'X_train': DataFrame,          # Training features
    'X_test': DataFrame,           # Test features
    'y_train': Series,             # Training target
    'y_test': Series,              # Test target
    'y_pred': ndarray,             # Predictions
    'numeric_features': list,      # Numeric features
    'categorical_features': list,  # Categorical features
    # ... more states
}
```

## Error Handling

1. **Validation Layer**: Di `data_handler.py`
   - File size validation
   - File format validation
   - Column existence validation

2. **Try-Catch Blocks**: Di semua page renderers
   - Graceful error messages
   - Detailed traceback for debugging

3. **User Guidance**: Warning & info messages
   - Missing features warning
   - Helpful tips on errors

## Performance Considerations

1. **Lazy Loading**: Dataset hanya di-load saat dibutuhkan
2. **Session Caching**: Results disimpan di session state
3. **Efficient Preprocessing**: ColumnTransformer untuk parallel processing
4. **n_jobs=-1**: Multiprocessing untuk Random Forest

## Extension Points

Untuk menambah fitur baru:

1. **New Page**: Tambah file di `app_pages/`
2. **New ML Model**: Tambah function di `ml_models/`
3. **New Utility**: Tambah function di `utils/`
4. **New Config**: Tambah constant di `config/settings.py`

## Testing Strategy

```
Unit Tests:
  - utils/data_handler.py
  - ml_models/preprocessing.py
  - ml_models/training.py

Integration Tests:
  - app_pages/*.py dengan mock session state

End-to-End Tests:
  - Full user flow dari upload sampai prediksi
```

## Best Practices

1. **Single Responsibility**: Setiap modul punya satu tanggung jawab
2. **DRY (Don't Repeat Yourself)**: Reuse functions
3. **Clear Naming**: Function & variable names yang jelas
4. **Documentation**: Docstrings untuk semua functions
5. **Type Hints**: Untuk parameter & return values
6. **Error Messages**: User-friendly error messages

