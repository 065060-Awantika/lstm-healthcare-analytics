import streamlit as st

st.set_page_config(
    page_title="LSTM Healthcare Analytics",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Hide default streamlit page nav (removes home/forecast/ethics from sidebar)
st.markdown("""
<style>
st.markdown("""
<style>
[data-testid="stSidebarNav"] { display: none !important; }

.main-header {
    background: linear-gradient(135deg,#1a1a2e 0%,#16213e 50%,#0f3460 100%);
    padding:2rem; border-radius:12px;
    text-align:center; margin-bottom:2rem;
}
.main-header h1 { color:#e94560; font-size:2.2rem; margin:0; }
.main-header p  { color:#a8dadc; font-size:1rem; margin:0.5rem 0 0 0; }

.metric-card {
    background: linear-gradient(135deg,#667eea 0%,#764ba2 100%);
    padding:1.2rem; border-radius:10px;
    text-align:center; color:white !important;
    margin-bottom:1rem;
}
.metric-card h3 { font-size:1.8rem; margin:0; font-weight:700; color:white !important; }
.metric-card p  { font-size:0.85rem; margin:0.3rem 0 0 0; opacity:0.9; color:white !important; }

.info-box {
    background:#1a3a5c !important;
    border:1px solid #3498db !important;
    border-radius:8px;
    padding:1rem;
    margin:1rem 0;
    color:#ffffff !important;
}
.info-box * { color:#ffffff !important; }

.warning-box {
    background:#3d2e00 !important;
    border:1px solid #ffc107 !important;
    border-radius:8px;
    padding:1rem;
    margin:1rem 0;
    color:#ffe082 !important;
}
.warning-box * { color:#ffe082 !important; }

.success-box {
    background:#1a3d2b !important;
    border:1px solid #4caf50 !important;
    border-radius:8px;
    padding:1rem;
    margin:1rem 0;
    color:#a5d6a7 !important;
}
.success-box * { color:#a5d6a7 !important; }

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg,#1a1a2e 0%,#16213e 100%) !important;
}
section[data-testid="stSidebar"] .stRadio label {
    color: white !important;
    font-size: 1rem !important;
}
section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] li,
section[data-testid="stSidebar"] span {
    color: #a8dadc !important;
}

div[data-testid="stMarkdownContainer"] p { color: inherit; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="main-header">
    <h1>🏥 LSTM Healthcare Analytics Dashboard</h1>
    <p>Personal Care & Wellness Sentiment x Johnson & Johnson (JNJ) Stock Forecasting</p>
    <p style="color:#53d8fb;font-size:0.85rem;">
    Project 4 Capstone | LSTM Models for Business Decision-Making</p>
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("""
<div style="text-align:center;padding:1rem;
background:linear-gradient(135deg,#e94560,#0f3460);
border-radius:10px;margin-bottom:1.5rem;">
    <h2 style="color:white;margin:0;">🏥 LSTM Analytics</h2>
    <p style="color:#a8dadc;font-size:0.8rem;margin:0.3rem 0 0 0;">
    Healthcare | JNJ | Amazon</p>
</div>
""", unsafe_allow_html=True)

selected = st.sidebar.radio(
    "Navigate",
    ["🏠 Home",
     "📈 JNJ Stock Forecast",
     "💡 Business Recommendations",
     "📊 Model Performance",
     "⚖️ Ethics & Responsibility"],
    label_visibility="collapsed"
)

st.sidebar.markdown("""
---
**📋 Project Info**
- Domain: Healthcare
- Text: Amazon Reviews
- TS Data: JNJ Stock
- Models: LSTM, BiLSTM, GRU, CNN-LSTM

**🎯 Competency Goals**
CG1 | CG2 | CG3 | CG6
""")

if selected == "🏠 Home":
    from pages.home import render
elif selected == "📈 JNJ Stock Forecast":
    from pages.forecast import render
elif selected == "💡 Business Recommendations":
    from pages.recommendations import render
elif selected == "📊 Model Performance":
    from pages.performance import render
else:
    from pages.ethics import render

render()
