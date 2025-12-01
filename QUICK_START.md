# Quick Start Guide

## 🚀 Menjalankan Aplikasi

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run Aplikasi
```bash
streamlit run streamlit_calorie_app.py
```

### 3. Buka Browser
Aplikasi otomatis terbuka di `http://localhost:8501`

## 📁 Struktur File (Simplified)

```
TB-AKDAT/
│
├── streamlit_calorie_app.py    ← Main file (Jalankan ini!)
│
├── config/                     ← Konfigurasi
│   └── settings.py            (Default values, menu items)
│
├── styles/                     ← CSS Styling
│   └── custom_css.py          (Purple gradient theme)
│
├── utils/                      ← Helper Functions
│   ├── data_handler.py        (Load & validate data)
│   └── session_manager.py     (Session state management)
│
├── ml_models/                  ← Machine Learning
│   ├── preprocessing.py       (Data preprocessing)
│   └── training.py            (Model training & evaluation)
│
└── app_pages/                  ← UI Pages
    ├── dataset_page.py        (Upload dataset)
    ├── preprocessing_page.py  (Select features)
    ├── training_page.py       (Train model)
    ├── visualization_page.py  (Charts & graphs)
    └── analysis_page.py       (Predict calories)
```

## 🎯 Workflow Pengguna

```
1. DATASET
   ↓ Upload CSV file
   
2. PREPROCESSING
   ↓ Pilih target & fitur
   
3. TRAINING
   ↓ Atur hyperparameter & train
   
4. VISUALISASI
   ↓ Lihat hasil & charts
   
5. ANALISIS
   ↓ Prediksi untuk data pribadi
```

## 🔧 Modifikasi Aplikasi

### Tambah Halaman Baru
1. Buat file baru di `app_pages/`, misal `new_page.py`
2. Buat function `render_new_page()`
3. Import di `app_pages/__init__.py`
4. Tambah di `streamlit_calorie_app.py`

```python
# app_pages/new_page.py
import streamlit as st

def render_new_page():
    st.title("Halaman Baru")
    st.write("Konten halaman...")
```

```python
# app_pages/__init__.py
from .new_page import render_new_page

__all__ = [
    # ... existing ...
    'render_new_page'
]
```

```python
# streamlit_calorie_app.py
from app_pages import render_new_page

def render_current_page():
    # ... existing pages ...
    elif page == 'Halaman Baru':
        render_new_page()
```

### Tambah ML Model Baru
1. Buat file di `ml_models/`, misal `gradient_boosting.py`
2. Buat function untuk training & evaluation
3. Import di `app_pages/training_page.py`

```python
# ml_models/gradient_boosting.py
from sklearn.ensemble import GradientBoostingRegressor

def train_gb_model(X, y, **params):
    model = GradientBoostingRegressor(**params)
    # ... training logic ...
    return model
```

### Ubah Konfigurasi
Edit `config/settings.py`:

```python
# Ubah default values
DEFAULT_N_ESTIMATORS = 1000  # Dari 500 ke 1000
DEFAULT_MAX_DEPTH = 30       # Dari 20 ke 30

# Tambah menu item baru
MENU_ITEMS = {
    'Dataset': '📊',
    'Preprocessing': '⚙️',
    'Training Data': '📈',
    'Visualisasi Data': '📉',
    'Advanced Settings': '🔧'  # Baru!
}
```

### Ubah Styling
Edit `styles/custom_css.py`:

```python
# Ubah warna tema dari purple ke blue
def get_custom_css():
    return """
    <style>
        /* Ubah dari #8b5cf6 (purple) ke #3b82f6 (blue) */
        button[kind="primary"] {
            background-color: #3b82f6 !important;
        }
    </style>
    """
```

## 🐛 Troubleshooting

### Error: "ModuleNotFoundError"
```bash
# Install semua dependencies
pip install -r requirements.txt
```

### Error: "FileNotFoundError: exercise_dataset.csv"
```bash
# Pastikan dataset ada di folder yang sama dengan streamlit_calorie_app.py
# Atau upload manual lewat UI
```

### Error: "Session state key not found"
```bash
# Restart aplikasi (Ctrl+C lalu run ulang)
streamlit run streamlit_calorie_app.py
```

### Aplikasi lemot
```python
# Kurangi n_estimators di config/settings.py
DEFAULT_N_ESTIMATORS = 100  # Dari 500 ke 100
```

## 📊 Sample Dataset Format

File CSV harus punya kolom berikut:

```csv
Exercise,Duration,BMI,Age,Heart Rate,Exercise Intensity,Actual Weight,Gender,Calories Burn
Running,30,22.5,25,140,8,70,male,350
Cycling,45,24.1,30,120,6,65,female,280
...
```

**Kolom Penting**:
- **Target**: `Calories Burn` (yang akan diprediksi)
- **Fitur**: Semua kolom lain kecuali `ID`, `Dream Weight`

## 🎓 Best Practices

1. **Upload Data**: Gunakan dataset min. 100 baris untuk hasil optimal
2. **Feature Selection**: Pilih fitur yang relevan (Weight, Gender, Age, Duration, Intensity)
3. **Hyperparameter**: Mulai dengan default, tuning jika perlu
4. **Model Evaluation**: R² > 0.8 = good, < 0.5 = poor
5. **Feature Importance**: Periksa fitur mana yang paling berpengaruh

## 📚 Resources

- **README.md**: Overview project
- **ARCHITECTURE.md**: Technical architecture
- **MIGRATION_GUIDE.md**: Perubahan dari versi lama
- **requirements.txt**: List dependencies

## 💡 Tips

1. **GPU Support**: Random Forest tidak butuh GPU, CPU sudah cukup
2. **Memory**: Dataset < 200MB untuk performa optimal
3. **Browser**: Chrome/Firefox recommended
4. **Screen**: Min. 1280x720 untuk UI optimal

## 🆘 Need Help?

1. Baca **ARCHITECTURE.md** untuk memahami struktur
2. Baca **MIGRATION_GUIDE.md** untuk melihat perubahan
3. Check linter errors: Tidak ada error di semua file
4. Compile check: Semua modul sudah di-compile successfully

---

**Happy Coding! 🌲**

