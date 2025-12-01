"""
Configuration settings for ForestCal application
"""

# Page configuration
PAGE_CONFIG = {
    'page_title': "ForestCal - Prediksi Kalori",
    'page_icon': "🌲",
    'layout': "wide",
    'initial_sidebar_state': "expanded"
}

# Menu items
MENU_ITEMS = {
    'Home': '',
    'Dataset': '',
    'Preprocessing': '',
    'Training Data': '',
    'Visualisasi Data': ''
}

# Default values
DEFAULT_TRAIN_SIZE = 0.65
DEFAULT_RANDOM_STATE = 42
DEFAULT_N_ESTIMATORS = 500
DEFAULT_MAX_DEPTH = 20
DEFAULT_MIN_SAMPLES_SPLIT = 5
DEFAULT_MIN_SAMPLES_LEAF = 2

# File constraints
MAX_FILE_SIZE_MB = 200

# Feature priority list
EXCLUDE_COLUMNS = ['ID', 'Dream Weight']
PRIORITY_WEIGHT_FEATURES = ['actual', 'weight']
PRIORITY_DEMOGRAPHIC = ['Gender', 'Age']
PRIORITY_EXERCISE = ['Duration', 'Exercise Intensity', 'Exercise', 'Heart Rate', 'BMI']
PRIORITY_ENVIRONMENTAL = ['Weather Conditions']

# Missing value strategies
MISSING_STRATEGIES = [
    'drop rows',
    'fill numeric mean',
    'fill numeric median',
    'fill with constant (0)'
]

