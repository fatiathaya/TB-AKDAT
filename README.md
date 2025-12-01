# ForestCal - Aplikasi Prediksi Pembakaran Kalori

Aplikasi berbasis Streamlit untuk analisis dan prediksi pembakaran kalori menggunakan Random Forest Regressor.

## Struktur Project

```
TB-AKDAT/
├── streamlit_calorie_app.py          # File utama (orchestrator)
├── config/
│   ├── __init__.py
│   └── settings.py                   # Konfigurasi aplikasi
├── styles/
│   ├── __init__.py
│   └── custom_css.py                 # CSS styling
├── utils/
│   ├── __init__.py
│   ├── data_handler.py               # Upload & data loading
│   └── session_manager.py            # Session state management
├── ml_models/
│   ├── __init__.py
│   ├── preprocessing.py              # Data preprocessing
│   └── training.py                   # Model training & evaluation
└── app_pages/
    ├── __init__.py
    ├── dataset_page.py               # Halaman Dataset
    ├── preprocessing_page.py         # Halaman Preprocessing
    ├── training_page.py              # Halaman Training
    ├── visualization_page.py         # Halaman Visualisasi
    └── analysis_page.py              # Halaman Analisis Pribadi
```

## Penjelasan Modul

### 1. **streamlit_calorie_app.py**
File utama yang mengatur routing halaman dan inisialisasi aplikasi.

### 2. **config/**
- `settings.py`: Konfigurasi global (default values, constraints, menu items)

### 3. **styles/**
- `custom_css.py`: Custom CSS untuk styling aplikasi

### 4. **utils/**
- `session_manager.py`: Mengelola session state Streamlit
- `data_handler.py`: Load, validasi, dan suggest kolom dataset

### 5. **ml_models/**
- `preprocessing.py`: Preprocessing data (missing values, scaling, encoding)
- `training.py`: Training Random Forest, evaluasi model, feature importance

### 6. **app_pages/**
- `dataset_page.py`: Upload & eksplorasi data
- `preprocessing_page.py`: Pemilihan fitur & target
- `training_page.py`: Hyperparameter tuning & training
- `visualization_page.py`: Visualisasi hasil prediksi
- `analysis_page.py`: Prediksi interaktif untuk data pribadi

## Cara Menjalankan

```bash
# Install dependencies
pip install streamlit pandas numpy scikit-learn matplotlib seaborn scipy

# Run aplikasi
streamlit run streamlit_calorie_app.py
```

## Fitur Utama

1. **Upload Dataset**: Drag & drop file CSV (max 200MB)
2. **Preprocessing**: Pilih fitur, handle missing values, encoding
3. **Training**: Hyperparameter tuning Random Forest
4. **Visualisasi**: Scatter plot, residual distribution, correlation heatmap
5. **Prediksi**: Prediksi interaktif untuk data pribadi

## Keuntungan Struktur Modular

1. **Maintainability**: Setiap modul fokus pada satu tanggung jawab
2. **Reusability**: Fungsi dapat digunakan ulang di berbagai bagian
3. **Scalability**: Mudah menambahkan fitur baru tanpa merusak kode existing
4. **Testability**: Setiap modul dapat ditest secara independen
5. **Readability**: Kode lebih mudah dibaca dan dipahami
6. **Collaboration**: Tim dapat bekerja pada modul berbeda secara paralel

## Requirements

- Python 3.8+
- streamlit
- pandas
- numpy
- scikit-learn
- matplotlib
- seaborn
- scipy

## Author

Dikembangkan untuk tugas mata kuliah Akuisisi Data

