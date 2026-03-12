import streamlit as st

st.set_page_config(
    page_title="LSTM Healthcare Analytics | JNJ",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=DM+Sans:wght@300;400;500;600&family=JetBrains+Mono:wght@400;600&display=swap');

[data-testid="stSidebarNav"] { display: none !important; }
#MainMenu, footer, header    { visibility: hidden; }
.block-container             { padding: 1.5rem 2rem !important; }

section[data-testid="stSidebar"] {
    display: block !important;
    visibility: visible !important;
    width: 280px !important;
    min-width: 280px !important;
    background: linear-gradient(180deg,#020d1a 0%,#041428 60%,#020d1a 100%) !important;
    border-right: 1px solid rgba(0,212,255,0.15) !important;
}
section[data-testid="stSidebar"] > div {
    display: block !important;
    visibility: visible !important;
}
[data-testid="collapsedControl"] { display: none !important; }
section[data-testid="stSidebar"]::before {
    content:''; position:absolute; top:0; left:0; right:0; height:3px;
    background: linear-gradient(90deg,#00d4ff,#f0b429,#ff4d6d); z-index:999;
}
section[data-testid="stSidebar"] * { color: #8bafc9 !important; }
section[data-testid="stSidebar"] .stRadio label {
    color: #e8f4fd !important; font-size: 0.95rem !important;
    font-weight: 500 !important; padding: 0.5rem 0.8rem !important;
    border-radius: 8px !important; display: block !important;
}

.stApp {
    background: #020b18 !important;
    background-image:
        radial-gradient(ellipse at 20% 0%, rgba(0,90,160,0.25) 0%, transparent 60%),
        radial-gradient(ellipse at 80% 100%, rgba(100,0,180,0.15) 0%, transparent 60%) !important;
}

.hero {
    background: linear-gradient(135deg,rgba(0,30,60,0.98) 0%,rgba(4,20,40,0.98) 100%);
    border: 1px solid rgba(0,212,255,0.2); border-radius: 20px;
    padding: 2.5rem 3rem; margin-bottom: 2rem;
    position: relative; overflow: hidden;
    box-shadow: 0 0 60px rgba(0,212,255,0.08);
}
.hero::before {
    content:''; position:absolute; top:-50%; left:-20%;
    width:60%; height:200%;
    background:radial-gradient(ellipse,rgba(0,212,255,0.07) 0%,transparent 70%);
    pointer-events:none;
}
.hero-eyebrow {
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.7rem; font-weight: 600; letter-spacing: 0.25em;
    color: #00d4ff !important; text-transform: uppercase;
    margin-bottom: 1rem; display: flex; align-items: center; gap: 0.75rem;
}
.hero-eyebrow::before {
    content:''; display:inline-block; width:32px; height:1px; background:#00d4ff;
}
.hero h1 {
    font-family: 'Playfair Display', serif !important;
    font-size: 2.8rem !important; font-weight: 900 !important;
    color: #e8f4fd !important; line-height: 1.15 !important;
    margin: 0 0 0.75rem 0 !important; letter-spacing: -0.02em !important;
}
.hero h1 span { color: #f0b429 !important; }
.hero-sub { font-size: 1rem; color: #8bafc9 !important; font-weight: 300; }
.hero-tags { display:flex; gap:0.6rem; margin-top:1.5rem; flex-wrap:wrap; }
.hero-tag {
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.68rem; padding: 0.3rem 0.85rem;
    border-radius: 20px; letter-spacing: 0.08em; font-weight: 600;
}
.tag-cyan   { background:rgba(0,212,255,0.1);   border:1px solid rgba(0,212,255,0.4);   color:#00d4ff !important; }
.tag-gold   { background:rgba(240,180,41,0.1);  border:1px solid rgba(240,180,41,0.4);  color:#f0b429 !important; }
.tag-rose   { background:rgba(255,77,109,0.1);  border:1px solid rgba(255,77,109,0.4);  color:#ff4d6d !important; }
.tag-green  { background:rgba(0,229,160,0.1);   border:1px solid rgba(0,229,160,0.4);   color:#00e5a0 !important; }
.tag-purple { background:rgba(176,106,255,0.1); border:1px solid rgba(176,106,255,0.4); color:#b06aff !important; }

.kpi-card {
    background: #071e33; border: 1px solid rgba(0,212,255,0.12);
    border-radius: 16px; padding: 1.4rem 1.2rem;
    position: relative; overflow: hidden; margin-bottom: 1rem;
}
.kpi-card::before { content:''; position:absolute; top:0; left:0; right:0; height:3px; }
.kpi-cyan::before  { background: linear-gradient(90deg,#00d4ff,transparent); }
.kpi-gold::before  { background: linear-gradient(90deg,#f0b429,transparent); }
.kpi-rose::before  { background: linear-gradient(90deg,#ff4d6d,transparent); }
.kpi-green::before { background: linear-gradient(90deg,#00e5a0,transparent); }
.kpi-icon  { font-size:1.5rem; margin-bottom:0.5rem; display:block; }
.kpi-value {
    font-family: 'Playfair Display', serif !important;
    font-size: 2.2rem; font-weight: 700; color: #e8f4fd !important;
    line-height: 1; margin-bottom: 0.3rem; display: block;
}
.kpi-label {
    font-size: 0.72rem; font-weight: 600; letter-spacing: 0.1em;
    text-transform: uppercase; color: #4a7a9b !important;
    display: block; margin-bottom: 0.15rem;
}
.kpi-sub {
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.7rem; color: #4a7a9b !important;
}

.info-box {
    background: linear-gradient(135deg,rgba(0,70,120,0.55),rgba(0,40,80,0.55)) !important;
    border: 1px solid rgba(0,212,255,0.2) !important;
    border-left: 3px solid #00d4ff !important;
    border-radius: 12px !important; padding: 1.2rem 1.5rem !important;
    margin: 1rem 0 !important; color: #e8f4fd !important;
}
.info-box * { color: #e8f4fd !important; }
.info-box strong { color: #00d4ff !important; }
.info-box em { color: #a8d8f0 !important; }

.warning-box {
    background: linear-gradient(135deg,rgba(100,60,0,0.55),rgba(70,35,0,0.55)) !important;
    border: 1px solid rgba(240,180,41,0.3) !important;
    border-left: 3px solid #f0b429 !important;
    border-radius: 12px !important; padding: 1.2rem 1.5rem !important;
    margin: 1rem 0 !important; color: #ffe0a0 !important;
}
.warning-box * { color: #ffe0a0 !important; }
.warning-box strong { color: #f0b429 !important; }

.success-box {
    background: linear-gradient(135deg,rgba(0,80,55,0.55),rgba(0,50,35,0.55)) !important;
    border: 1px solid rgba(0,229,160,0.25) !important;
    border-left: 3px solid #00e5a0 !important;
    border-radius: 12px !important; padding: 1.2rem 1.5rem !important;
    margin: 1rem 0 !important; color: #a0f0d8 !important;
}
.success-box * { color: #a0f0d8 !important; }
.success-box strong { color: #00e5a0 !important; }

[data-testid="stMetric"] {
    background: #071e33 !important;
    border: 1px solid rgba(0,212,255,0.12) !important;
    border-radius: 12px !important; padding: 1rem !important;
}
[data-testid="stMetricValue"] {
    font-family: 'Playfair Display', serif !important; color: #e8f4fd !important;
}
[data-testid="stMetricLabel"] { color: #8bafc9 !important; }

.stTabs [data-baseweb="tab-list"] {
    background: #041428 !important; border-radius: 12px !important;
    padding: 4px !important; border: 1px solid rgba(0,212,255,0.12) !important;
    gap: 4px !important;
}
.stTabs [data-baseweb="tab"] {
    border-radius: 8px !important; color: #8bafc9 !important;
    font-weight: 500 !important; font-size: 0.88rem !important;
}
.stTabs [aria-selected="true"] {
    background: linear-gradient(135deg,rgba(0,212,255,0.15),rgba(176,106,255,0.1)) !important;
    color: #00d4ff !important; border: 1px solid rgba(0,212,255,0.2) !important;
}

.stButton > button {
    background: linear-gradient(135deg,#00d4ff,#0099cc) !important;
    color: #000 !important; font-weight: 700 !important;
    border: none !important; border-radius: 10px !important;
}
.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 25px rgba(0,212,255,0.35) !important;
}

.stTextArea textarea {
    background: #071e33 !important; border: 1px solid rgba(0,212,255,0.2) !important;
    border-radius: 10px !important; color: #e8f4fd !important;
}
.stSelectbox > div > div {
    background: #071e33 !important; border: 1px solid rgba(0,212,255,0.2) !important;
    border-radius: 10px !important; color: #e8f4fd !important;
}
.stApp p, .stApp li { color: #8bafc9 !important; }
.stApp h1, .stApp h2, .stApp h3 {
    font-family: 'Playfair Display', serif !important; color: #e8f4fd !important;
}
hr { border-color: rgba(0,212,255,0.1) !important; margin: 1.5rem 0 !important; }
.stDataFrame { border-radius: 12px !important; overflow: hidden !important; }
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <div class="hero-eyebrow">Project 4 Capstone &nbsp;|&nbsp; Deep Learning Analytics</div>
    <h1>LSTM <span>Healthcare</span> Analytics Dashboard</h1>
    <p class="hero-sub">Personal Care &amp; Wellness Sentiment &times; Johnson &amp; Johnson Stock Forecasting</p>
    <div class="hero-tags">
        <span class="hero-tag tag-cyan">LSTM</span>
        <span class="hero-tag tag-gold">BiLSTM</span>
        <span class="hero-tag tag-rose">Attention</span>
        <span class="hero-tag tag-green">CNN-LSTM</span>
        <span class="hero-tag tag-purple">GRU</span>
        <span class="hero-tag tag-cyan">JNJ Stock</span>
        <span class="hero-tag tag-gold">Amazon Reviews</span>
    </div>
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("""
<div style="background:linear-gradient(135deg,rgba(0,212,255,0.1),rgba(176,106,255,0.1));
border:1px solid rgba(0,212,255,0.2);border-radius:14px;
padding:1.2rem;text-align:center;margin-bottom:1.5rem;">
<div style="font-size:2rem;">&#x1F3E5;</div>
<div style="font-family:'Playfair Display',serif !important;font-size:1.1rem;
color:#e8f4fd !important;font-weight:700;margin:0.4rem 0 0.2rem 0;">LSTM Analytics</div>
<div style="font-family:'JetBrains Mono',monospace !important;font-size:0.6rem;
letter-spacing:0.15em;color:#00d4ff !important;">HEALTHCARE | JNJ | NLP</div>
</div>
""", unsafe_allow_html=True)

selected = st.sidebar.radio(
    "Navigate",
    [
        "🏠  Home",
        "📈  JNJ Stock Forecast",
        "💡  Business Recommendations",
        "📊  Model Performance",
        "⚖️  Ethics and Responsibility"
    ],
    label_visibility="collapsed"
)

st.sidebar.markdown("""
<div style="margin-top:1rem;padding:1rem;
background:rgba(0,212,255,0.04);
border:1px solid rgba(0,212,255,0.12);border-radius:12px;">
<div style="font-family:'JetBrains Mono',monospace !important;font-size:0.6rem;
letter-spacing:0.15em;color:#00d4ff !important;
text-transform:uppercase;margin-bottom:0.8rem;">Project Info</div>
<div style="font-size:0.82rem;color:#8bafc9 !important;margin:0.3rem 0;">&#x1F3E5; Domain: Healthcare</div>
<div style="font-size:0.82rem;color:#8bafc9 !important;margin:0.3rem 0;">&#x1F4DD; Text: Amazon Reviews</div>
<div style="font-size:0.82rem;color:#8bafc9 !important;margin:0.3rem 0;">&#x1F4C8; TS: JNJ Stock 2015-2024</div>
<div style="font-size:0.82rem;color:#8bafc9 !important;margin:0.3rem 0;">&#x1F9E0; LSTM · BiLSTM · GRU · CNN</div>
</div>
<div style="margin-top:0.8rem;padding:1rem;
background:rgba(240,180,41,0.04);
border:1px solid rgba(240,180,41,0.15);border-radius:12px;">
<div style="font-family:'JetBrains Mono',monospace !important;font-size:0.6rem;
letter-spacing:0.15em;color:#f0b429 !important;
text-transform:uppercase;margin-bottom:0.6rem;">Competency Goals</div>
<div style="font-size:0.85rem;color:#8bafc9 !important;">CG1 &nbsp;·&nbsp; CG2 &nbsp;·&nbsp; CG3 &nbsp;·&nbsp; CG6</div>
</div>
""", unsafe_allow_html=True)

if "Home" in selected:
    from pages.home import render
elif "Stock Forecast" in selected:
    from pages.forecast import render
elif "Recommendations" in selected:
    from pages.recommendations import render
elif "Performance" in selected:
    from pages.performance import render
else:
    from pages.ethics import render

render()
