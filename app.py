import streamlit as st

st.set_page_config(
    page_title="LSTM Healthcare Analytics | JNJ",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=DM+Sans:wght@300;400;500;600&family=JetBrains+Mono:wght@400;600&display=swap');

[data-testid="stSidebarNav"]  { display: none !important; }
[data-testid="stSidebar"]     { display: none !important; }
[data-testid="collapsedControl"] { display: none !important; }
#MainMenu, footer, header     { visibility: hidden; }
.block-container              { padding: 0.5rem 2rem 2rem !important; }

.stApp {
    background: #020b18 !important;
    background-image:
        radial-gradient(ellipse at 20% 0%,   rgba(0,90,160,0.25)  0%, transparent 60%),
        radial-gradient(ellipse at 80% 100%, rgba(100,0,180,0.15) 0%, transparent 60%) !important;
}

/* ── TOP NAV BAR ── */
.topnav {
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: rgba(4,20,40,0.95);
    border: 1px solid rgba(0,212,255,0.15);
    border-radius: 14px;
    padding: 0.7rem 1.5rem;
    margin-bottom: 1.5rem;
    backdrop-filter: blur(10px);
    position: sticky;
    top: 0;
    z-index: 999;
}
.topnav-brand {
    font-family: 'Playfair Display', serif;
    font-size: 1rem;
    font-weight: 700;
    color: #e8f4fd;
    display: flex;
    align-items: center;
    gap: 0.5rem;
    white-space: nowrap;
}
.topnav-brand span { color: #f0b429; }
.topnav-links {
    display: flex;
    gap: 0.3rem;
    flex-wrap: nowrap;
}
.nav-btn {
    font-family: 'DM Sans', sans-serif;
    font-size: 0.82rem;
    font-weight: 500;
    padding: 0.4rem 0.9rem;
    border-radius: 8px;
    border: 1px solid transparent;
    cursor: pointer;
    color: #8bafc9;
    background: transparent;
    transition: all 0.2s;
    white-space: nowrap;
}
.nav-btn:hover {
    background: rgba(0,212,255,0.08);
    color: #00d4ff;
    border-color: rgba(0,212,255,0.2);
}
.nav-btn-active {
    background: linear-gradient(135deg,rgba(0,212,255,0.15),rgba(176,106,255,0.1));
    color: #00d4ff !important;
    border-color: rgba(0,212,255,0.3) !important;
}

/* ── HERO ── */
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
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.7rem; font-weight: 600; letter-spacing: 0.25em;
    color: #00d4ff; text-transform: uppercase;
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
.hero-sub { font-size: 1rem; color: #8bafc9; font-weight: 300; }
.hero-tags { display:flex; gap:0.6rem; margin-top:1.5rem; flex-wrap:wrap; }
.hero-tag {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.68rem; padding: 0.3rem 0.85rem;
    border-radius: 20px; letter-spacing: 0.08em; font-weight: 600;
}
.tag-cyan   { background:rgba(0,212,255,0.1);   border:1px solid rgba(0,212,255,0.4);   color:#00d4ff; }
.tag-gold   { background:rgba(240,180,41,0.1);  border:1px solid rgba(240,180,41,0.4);  color:#f0b429; }
.tag-rose   { background:rgba(255,77,109,0.1);  border:1px solid rgba(255,77,109,0.4);  color:#ff4d6d; }
.tag-green  { background:rgba(0,229,160,0.1);   border:1px solid rgba(0,229,160,0.4);   color:#00e5a0; }
.tag-purple { background:rgba(176,106,255,0.1); border:1px solid rgba(176,106,255,0.4); color:#b06aff; }

/* ── KPI CARDS ── */
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
    font-size: 2.2rem; font-weight: 700; color: #e8f4fd;
    line-height: 1; margin-bottom: 0.3rem; display: block;
}
.kpi-label {
    font-size: 0.72rem; font-weight: 600; letter-spacing: 0.1em;
    text-transform: uppercase; color: #4a7a9b; display: block; margin-bottom: 0.15rem;
}
.kpi-sub { font-family:'JetBrains Mono',monospace; font-size:0.7rem; color:#4a7a9b; }

/* ── INFO BOXES ── */
.info-box {
    background: linear-gradient(135deg,rgba(0,70,120,0.55),rgba(0,40,80,0.55));
    border: 1px solid rgba(0,212,255,0.2); border-left: 3px solid #00d4ff;
    border-radius: 12px; padding: 1.2rem 1.5rem; margin: 1rem 0;
}
.info-box, .info-box p, .info-box span, .info-box li { color: #e8f4fd !important; }
.info-box strong { color: #00d4ff !important; }
.info-box em { color: #a8d8f0 !important; }

.warning-box {
    background: linear-gradient(135deg,rgba(100,60,0,0.55),rgba(70,35,0,0.55));
    border: 1px solid rgba(240,180,41,0.3); border-left: 3px solid #f0b429;
    border-radius: 12px; padding: 1.2rem 1.5rem; margin: 1rem 0;
}
.warning-box, .warning-box p, .warning-box span { color: #ffe0a0 !important; }
.warning-box strong { color: #f0b429 !important; }

.success-box {
    background: linear-gradient(135deg,rgba(0,80,55,0.55),rgba(0,50,35,0.55));
    border: 1px solid rgba(0,229,160,0.25); border-left: 3px solid #00e5a0;
    border-radius: 12px; padding: 1.2rem 1.5rem; margin: 1rem 0;
}
.success-box, .success-box p, .success-box span { color: #a0f0d8 !important; }
.success-box strong { color: #00e5a0 !important; }

[data-testid="stMetric"] {
    background: #071e33 !important; border: 1px solid rgba(0,212,255,0.12) !important;
    border-radius: 12px !important; padding: 1rem !important;
}
[data-testid="stMetricValue"] {
    font-family: 'Playfair Display', serif !important; color: #e8f4fd !important;
}
[data-testid="stMetricLabel"] { color: #8bafc9 !important; }

.stTabs [data-baseweb="tab-list"] {
    background: #041428 !important; border-radius: 12px !important;
    padding: 4px !important; border: 1px solid rgba(0,212,255,0.12) !important; gap: 4px !important;
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
    background: rgba(4,20,40,0.9) !important;
    color: #8bafc9 !important;
    font-weight: 500 !important;
    border: 1px solid rgba(0,212,255,0.2) !important;
    border-radius: 10px !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 0.88rem !important;
    transition: all 0.2s !important;
}
.stButton > button:hover {
    background: rgba(0,212,255,0.1) !important;
    color: #00d4ff !important;
    border-color: rgba(0,212,255,0.4) !important;
    transform: translateY(-1px) !important;
}
.stButton > button[kind="primary"] {
    background: linear-gradient(135deg,rgba(0,212,255,0.2),rgba(176,106,255,0.15)) !important;
    color: #00d4ff !important;
    border: 1px solid rgba(0,212,255,0.4) !important;
    font-weight: 700 !important;
}
.stTextArea textarea {
    background: #071e33 !important; border: 1px solid rgba(0,212,255,0.2) !important;
    border-radius: 10px !important; color: #e8f4fd !important;
}
.stSelectbox > div > div {
    background: #071e33 !important; border: 1px solid rgba(0,212,255,0.2) !important;
    border-radius: 10px !important; color: #e8f4fd !important;
}
.stApp h1, .stApp h2, .stApp h3 {
    font-family: 'Playfair Display', serif !important; color: #e8f4fd !important;
}
.stApp p, .stApp li { color: #8bafc9; }
hr { border-color: rgba(0,212,255,0.1) !important; margin: 1.5rem 0 !important; }
.stDataFrame { border-radius: 12px !important; }
</style>
""", unsafe_allow_html=True)

# ── SESSION STATE FOR PAGE ────────────────────────────────────────────────────
if "page" not in st.session_state:
    st.session_state.page = "Home"

PAGES = ["Home", "JNJ Stock Forecast", "Business Recommendations", "Model Performance", "Ethics"]
ICONS = ["🏠", "📈", "💡", "📊", "⚖️"]

# ── TOP NAVIGATION BAR ────────────────────────────────────────────────────────
st.markdown("""
<div class="topnav">
    <div class="topnav-brand">🏥 &nbsp; LSTM <span>Healthcare</span> &nbsp;|&nbsp; JNJ Analytics</div>
</div>
""", unsafe_allow_html=True)

# Native Streamlit nav buttons in columns
nav_cols = st.columns(len(PAGES))
for i, (col, page, icon) in enumerate(zip(nav_cols, PAGES, ICONS)):
    with col:
        label = f"{icon} {page}"
        is_active = st.session_state.page == page
        if st.button(
            label,
            key=f"nav_{i}",
            use_container_width=True,
            type="primary" if is_active else "secondary"
        ):
            st.session_state.page = page
            st.rerun()

st.markdown("<div style='margin-bottom:1rem'></div>", unsafe_allow_html=True)

# ── HERO ─────────────────────────────────────────────────────────────────────
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

# ── ROUTING ───────────────────────────────────────────────────────────────────
page = st.session_state.page

if page == "Home":
    from pages.home import render
elif page == "JNJ Stock Forecast":
    from pages.forecast import render
elif page == "Business Recommendations":
    from pages.recommendations import render
elif page == "Model Performance":
    from pages.performance import render
else:
    from pages.ethics import render

render()
