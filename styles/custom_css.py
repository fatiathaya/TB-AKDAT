"""
Custom CSS styling for ForestCal application
"""

def get_custom_css():
    """Return custom CSS as string"""
    return """
<style>
    /* Main background */
    .stApp {
        background: linear-gradient(135deg, #2d1b4e 0%, #1a0d2e 100%);
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #4a2c7a 0%, #2d1b4e 100%);
    }
    
    [data-testid="stSidebar"] .css-1d391kg {
        padding-top: 0rem;
    }
    
    /* Sidebar menu items */
    .sidebar-menu-item {
        padding: 0.75rem 1rem;
        margin: 0.25rem 0;
        border-radius: 8px;
        cursor: pointer;
        transition: all 0.3s;
        color: white;
        display: flex;
        align-items: center;
        gap: 0.75rem;
    }
    
    .sidebar-menu-item:hover {
        background-color: rgba(255, 255, 255, 0.1);
    }
    
    .sidebar-menu-item.active {
        background-color: rgba(255, 255, 255, 0.2);
        font-weight: bold;
    }
    
    /* Logo - Modern Professional Typography */
    .logo {
        font-size: 2.2rem;
        font-weight: 800;
        text-align: center;
        padding: 1.5rem 0;
        margin-bottom: 2rem;
        letter-spacing: -0.02em;
        background: linear-gradient(135deg, #a78bfa 0%, #ec4899 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', sans-serif;
        position: relative;
        text-transform: uppercase;
        line-height: 1.2;
        text-shadow: 0 0 30px rgba(167, 139, 250, 0.3);
        transition: all 0.3s ease;
    }
    
    .logo:hover {
        transform: scale(1.02);
        filter: brightness(1.1);
    }
    
    .logo::before {
        content: '';
        position: absolute;
        top: 0;
        left: 50%;
        transform: translateX(-50%);
        width: 60px;
        height: 2px;
        background: linear-gradient(90deg, transparent, #8b5cf6, transparent);
        border-radius: 2px;
        opacity: 0.6;
    }
    
    .logo::after {
        content: '';
        position: absolute;
        bottom: 0.8rem;
        left: 50%;
        transform: translateX(-50%);
        width: 50px;
        height: 2px;
        background: linear-gradient(90deg, #8b5cf6, #ec4899);
        border-radius: 2px;
        opacity: 0.8;
    }
    
    /* Main content styling */
    .main-content {
        color: white;
    }
    
    /* Section headers */
    h1, h2, h3 {
        color: white !important;
    }
    
    /* Upload area styling */
    .upload-area {
        border: 2px dashed #8b5cf6;
        border-radius: 12px;
        padding: 3rem 2rem;
        text-align: center;
        background-color: rgba(139, 92, 246, 0.1);
        margin: 1rem 0;
        cursor: pointer;
        transition: all 0.3s;
    }
    
    .upload-area:hover {
        background-color: rgba(139, 92, 246, 0.2);
        border-color: #a78bfa;
    }
    
    /* Global button styling (non-sidebar) */
    .stButton>button {
        border-radius: 8px;
        font-weight: 500;
        transition: all 0.25s ease;
    }
    
    .stButton>button:hover {
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.35);
    }
    
    /* Sidebar navigation buttons - modern pill style */
    [data-testid="stSidebar"] .stButton>button {
        width: 100%;
        justify-content: flex-start;
        border-radius: 999px;
        padding: 0.6rem 1rem;
        font-size: 0.95rem;
        border: 1px solid transparent;
        background: transparent;
        color: #e5e7eb;
        box-shadow: none;
    }
    
    [data-testid="stSidebar"] .stButton>button[kind="secondary"] {
        background: linear-gradient(90deg, rgba(148, 163, 184, 0.15), rgba(30, 64, 175, 0.0));
    }
    
    [data-testid="stSidebar"] .stButton>button[kind="secondary"]:hover {
        background: linear-gradient(90deg, rgba(129, 140, 248, 0.45), rgba(59, 130, 246, 0.15));
        border-color: rgba(129, 140, 248, 0.7);
        transform: translateY(-1px);
        box-shadow: 0 8px 18px rgba(15, 23, 42, 0.75);
    }
    
    [data-testid="stSidebar"] .stButton>button[kind="primary"] {
        background: linear-gradient(90deg, #8b5cf6, #ec4899);
        border-color: rgba(248, 250, 252, 0.5);
        color: white;
        box-shadow: 0 10px 25px rgba(139, 92, 246, 0.6);
    }
    
    [data-testid="stSidebar"] .stButton>button[kind="primary"]:hover {
        filter: brightness(1.05);
        transform: translateY(-1px);
        box-shadow: 0 14px 30px rgba(139, 92, 246, 0.9);
    }
    
    /* Table styling */
    .dataframe {
        background-color: white;
        color: black;
    }
    
    /* Info boxes - compact and modern */
    .info-box {
        background: linear-gradient(135deg, rgba(139, 92, 246, 0.15), rgba(236, 72, 153, 0.1));
        border-left: 3px solid #8b5cf6;
        border-radius: 8px;
        padding: 0.6rem 1rem;
        margin: 0.4rem 0;
        display: flex;
        align-items: center;
        transition: all 0.3s ease;
    }
    
    .info-box:hover {
        background: linear-gradient(135deg, rgba(139, 92, 246, 0.25), rgba(236, 72, 153, 0.15));
        border-left: 3px solid #a78bfa;
        transform: translateX(3px);
    }
    
    .info-box p {
        margin: 0;
        font-size: 0.95rem;
        font-weight: 500;
        color: #e5e7eb;
    }
    
    /* Card styling - Satu garis pemisah di bawah saja, spacing minimal */
    .preprocessing-card {
        background: transparent;
        border: none;
        border-bottom: 1px solid rgba(139, 92, 246, 0.2);
        border-radius: 0;
        padding: 0;
        padding-bottom: 1.2rem;
        margin: 0;
        margin-bottom: 1.2rem;
        color: white;
        transition: all 0.3s ease;
    }
    
    .preprocessing-card:hover {
        border-bottom-color: rgba(139, 92, 246, 0.35);
    }
    
    /* Hilangkan border kotak Streamlit */
    [data-testid="stVerticalBlock"] > div[style*="border"] {
        border: none !important;
        border-radius: 0 !important;
    }
    
    .preprocessing-card h3 {
        color: white !important;
        margin-bottom: 1rem;
        font-size: 1.2rem;
        font-weight: 600;
    }
    
    .preprocessing-card p {
        color: white;
        margin: 0.5rem 0;
        font-size: 1rem;
    }
    
    .preprocessing-card ul {
        color: white;
        margin: 0.5rem 0;
        padding-left: 1.5rem;
    }
    
    .preprocessing-card li {
        color: white;
        margin: 0.25rem 0;
    }
    
    /* Info Note - Modern Alert Style */
    .info-note {
        background: rgba(139, 92, 246, 0.1);
        border: 1px solid rgba(139, 92, 246, 0.3);
        border-radius: 8px;
        padding: 0.9rem 1.1rem;
        margin-top: 1.2rem;
        color: #e0e7ff;
        font-size: 0.88rem;
        line-height: 1.6;
    }
    
    .info-note strong {
        color: white;
    }
    
    /* Multiselect tag warna ungu */
    span[data-baseweb="tag"] {
        background-color: rgba(139, 92, 246, 0.8) !important;
        border: 1px solid rgba(139, 92, 246, 0.9) !important;
    }
    
    span[data-baseweb="tag"] span {
        color: white !important;
    }
    
    /* Close button pada tag */
    span[data-baseweb="tag"] svg {
        fill: white !important;
    }
    
    /* Training page styling - Satu garis pemisah di bawah, spacing minimal */
    .training-section {
        margin: 0;
        margin-bottom: 1.2rem;
        padding: 0;
        padding-bottom: 1.2rem;
        background: transparent;
        border: none;
        border-bottom: 1px solid rgba(139, 92, 246, 0.2);
        border-radius: 0;
        transition: all 0.3s ease;
    }
    
    .training-section:hover {
        border-bottom-color: rgba(139, 92, 246, 0.35);
    }
    
    .training-section h3 {
        color: white !important;
        margin-bottom: 1rem;
        font-size: 1.1rem;
        font-weight: 600;
    }
    
    /* Button styling - Ubah dari oren ke ungu */
    button[kind="primary"] {
        background-color: #8b5cf6 !important;
        border-color: #7c3aed !important;
        color: white !important;
    }
    
    button[kind="primary"]:hover {
        background-color: #7c3aed !important;
        border-color: #6d28d9 !important;
    }
    
    button[kind="primary"]:active {
        background-color: #6d28d9 !important;
    }
    
    /* Secondary buttons */
    button[kind="secondary"] {
        background-color: rgba(139, 92, 246, 0.1) !important;
        border-color: rgba(139, 92, 246, 0.3) !important;
        color: white !important;
    }
    
    button[kind="secondary"]:hover {
        background-color: rgba(139, 92, 246, 0.2) !important;
        border-color: rgba(139, 92, 246, 0.5) !important;
    }
    
    /* Slider track - Ubah dari oren ke ungu */
    .stSlider > div > div > div > div {
        background-color: #8b5cf6 !important;
    }
    
    div[data-baseweb="slider"] > div > div {
        background-color: #8b5cf6 !important;
    }
    
    /* Slider thumb (bulatan) */
    div[data-baseweb="slider"] [role="slider"] {
        background-color: #7c3aed !important;
        border-color: #8b5cf6 !important;
    }
    
    div[data-baseweb="slider"] [role="slider"]:hover {
        box-shadow: 0 0 0 0.2rem rgba(139, 92, 246, 0.5) !important;
        background-color: #8b5cf6 !important;
    }
    
    /* ANGKA SLIDER - Force override dari oren ke ungu */
    .stSlider div[data-testid="stThumbValue"],
    .stSlider div[data-testid="stThumbValue"] > div,
    .stSlider div[data-testid="stThumbValue"] p,
    .stSlider div[data-testid="stThumbValue"] span {
        color: #c4b5fd !important;
        background: transparent !important;
    }
    
    /* Target semua text di dalam slider */
    .stSlider div > div > div > div[style] {
        color: #c4b5fd !important;
    }
    
    /* Override inline styles rgb(255, ...) */
    .stSlider [style*="color: rgb(255"] {
        color: #c4b5fd !important;
    }
    
    /* Min-max labels */
    .stSlider [data-testid="stTickBarMin"],
    .stSlider [data-testid="stTickBarMax"] {
        color: rgba(255, 255, 255, 0.5) !important;
    }
    
    /* Progress bar - Ubah dari oren ke ungu */
    .stProgress > div > div > div > div {
        background-color: #8b5cf6 !important;
    }
    
    /* CHECKBOX - Ubah dari oren ke ungu, hilangkan background */
    span[data-baseweb="checkbox"] > div:first-child {
        background-color: #8b5cf6 !important;
        border-color: #8b5cf6 !important;
    }
    
    span[data-baseweb="checkbox"][aria-checked="true"] > div:first-child {
        background-color: #8b5cf6 !important;
        border-color: #8b5cf6 !important;
    }
    
    span[data-baseweb="checkbox"] svg {
        fill: white !important;
    }
    
    div[data-testid="stCheckbox"] > label {
        background: transparent !important;
        background-color: transparent !important;
    }
    
    div[data-testid="stCheckbox"] {
        background: transparent !important;
        background-color: transparent !important;
    }
    
    div[data-testid="stCheckbox"] > label > div {
        background: transparent !important;
        background-color: transparent !important;
    }
    
    div[data-testid="stCheckbox"] label span {
        color: white !important;
    }
    
    /* Selectbox focus */
    div[data-baseweb="select"] > div:focus-within {
        border-color: #8b5cf6 !important;
        box-shadow: 0 0 0 0.2rem rgba(139, 92, 246, 0.25) !important;
    }
    
    /* Number input focus */
    input[type="number"]:focus {
        border-color: #8b5cf6 !important;
        box-shadow: 0 0 0 0.2rem rgba(139, 92, 246, 0.25) !important;
    }
    
    /* GLOBAL COLOR OVERRIDE: SEMUA OREN → UNGU */
    [style*="color: rgb(255, 75, 75)"],
    [style*="color: rgb(255, 43, 43)"],
    [style*="color: rgb(240, 75, 75)"],
    [style*="color: #ff4b4b"],
    [style*="color: #ff2b2b"] {
        color: #c4b5fd !important;
    }
    
    [style*="background-color: rgb(255, 75, 75)"],
    [style*="background-color: rgb(255, 43, 43)"],
    [style*="background: rgb(255, 75, 75)"],
    [style*="background: rgb(255, 43, 43)"] {
        background-color: #8b5cf6 !important;
        background: #8b5cf6 !important;
    }
    
    .stAlert[data-baseweb="notification"] {
        background-color: rgba(139, 92, 246, 0.1) !important;
        border-color: #8b5cf6 !important;
    }
    
    .stSuccess {
        background-color: rgba(34, 197, 94, 0.1) !important;
        border-left-color: #22c55e !important;
    }
    
    .stInfo {
        background-color: rgba(59, 130, 246, 0.1) !important;
        border-left-color: #3b82f6 !important;
    }
    
    input[type="text"],
    input[type="number"],
    textarea,
    select {
        color: white !important;
    }
    
    [data-baseweb="menu"] [role="option"] {
        color: #1f2937 !important;
    }
    
    [data-baseweb="menu"] [role="option"]:hover {
        background-color: rgba(139, 92, 246, 0.2) !important;
    }
    
    /* Hide Streamlit default elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
"""

