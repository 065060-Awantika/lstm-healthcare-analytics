import streamlit as st

st.set_page_config(
    page_title="LSTM Healthcare Analytics | JNJ",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=DM+Sans:wght@300;400;500;600&family=JetBrains+Mono:wght@400;600&display=swap');

:root {
    --bg-primary:    #020b18;
    --bg-secondary:  #041428;
    --bg-card:       #071e33;
    --bg-glass:      rgba(6,28,54,0.85);
    --accent-gold:   #f0b429;
    --accent-cyan:   #00d4ff;
    --accent-rose:   #ff4d6d;
    --accent-green:  #00e5a0;
    --accent-purple: #b06aff;
    --text-primary:  #e8f4fd;
    --text-secondary:#8bafc9;
    --text-muted:    #4a7a9b;
    --border:        rgba(0,212,255,0.15);
}

* { font-family: 'DM Sans', sans-serif !important; box-sizing: border-box; }

[data-testid="stSidebarNav"] { display: none !important; }
#MainMenu, footer, header    { visibility: hidden; }
.block-container             { padding: 1.5rem 2rem !important; }

.stApp {
    background: var(--bg-primary);
    background-image:
        radial-gradient(ellipse at 20% 0%,   rgba(0,90,160,0.25)  0%, transparent 60%),
        radial-gradient(ellipse at 80% 100%, rgba(100,0,180,0.15) 0%, transparent 60%);
}

/* ── SIDEBAR ── */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg,#020d1a 0%,#041428 60%,#020d1a 100%) !important;
    border-right: 1px solid rgba(0,212,255,0.12) !important;
}
section[data-testid="stSidebar"]::before {
    content:'';
    position:absolute; top:0; left:0; right:0; height:3px;
    background:linear-gradient(90deg,#00d4ff,#f0b429,#ff4d6d);
}
section[data-testid="stSidebar"] * { color: var(--text-secondary) !important; }
section[data-testid="stSidebar"] .stRadio label {
    color: #e8f4fd !important;
    font-size: 0.92rem !important;
    font-weight: 500 !important;
    padding: 0.4rem 0 !important;
}

/* ── HERO ── */
.hero {
    background: linear-gradient(135deg,rgba(0,30,60,0.98) 0%,rgba(4,20,40,0.98) 100%);
    border: 1px solid rgba(0,212,255,0.2);
    border-radius: 20px;
    padding: 3rem;
    margin-bottom: 2rem;
    position: relative;
    overflow: hidden;
    box-shadow: 0 0 60px rgba(0,212,255,0.08), inset 0 1px 0 rgba(255,255,255,0.04);
}
.hero::before {
    content:'';
    position:absolute; top:-50%; left:-20%;
    width:60%; height:200%;
    background:radial-gradient(ellipse,rgba(0,212,255,0.07) 0%,transparent 70%);
}
.hero::after {
    content:'';
    position:absolute; bottom:-50%; right:-10%;
    width:50%; height:200%;
    background:radial-gradient(ellipse,rgba(176,106,255,0.07) 0%,transparent 70%);
}
.hero-eyebrow {
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.7rem;
    font-weight: 600;
    letter-spacing: 0.25em;
    color: #00d4ff;
    text-transform: uppercase;
    margin-bottom: 1rem;
    display: flex;
    align-items: center;
    gap: 0.75rem;
}
.hero-eyebrow::before {
    content:''; display:inline-block;
    width:32px; height:1px; background:#00d4ff;
}
.hero h1 {
    font-family: 'Playfair Display', serif !important;
    font-size: 3rem !important;
    font-weight: 900 !important;
    color: #e8f4fd !important;
    line-height: 1.1 !important;
    margin: 0 0 0.75rem 0 !important;
    letter-spacing: -0.02em !important;
}
.hero h1 span { color: #f0b429; }
.hero-sub {
    font-size: 1rem;
    color: #8bafc9;
    font-weight: 300;
    letter-spacing: 0.03em;
}
.hero-tags {
    display:flex; gap:0.6rem;
    margin-top:1.5rem; flex-wrap:wrap;
}
.hero-tag {
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.68rem;
    padding: 0.3rem 0.85rem;
    border-radius: 20px;
    letter-spacing: 0.1em;
    font-weight: 600;
}
.tag-cyan   {background:rgba(0,212,255,0.1);  border:1px solid rgba(0,212,255,0.35);  color:#00d4ff;}
.tag-gold   {background:rgba(240,180,41,0.1); border:1px solid rgba(240,180,41,0.35); color:#f0b429;}
.tag-rose   {background:rgba(255,77,109,0.1); border:1px solid rgba(255,77,109,0.35); color:#ff4d6d;}
.tag-green  {background:rgba(0,229,160,0.1);  border:1px solid rgba(0,229,160,0.35);  color:#00e5a0;}
.tag-purple {background:rgba(176,106,255,0.1);border:1px solid rgba(176,106,255,0.35);color:#b06aff;}

/* ── KPI CARDS ── */
.kpi-card {
    background: #071e33;
    border: 1px solid rgba(0,212,255,0.12);
    border-radius: 16px;
    padding: 1.4rem 1.2rem;
    position: relative;
    overflow: hidden;
    height: 100%;
}
.kpi-card::before {
    content:'';
    position:absolute; top:0; left:0; right:0; height:2px;
}
.kpi-cyan::before   {background:linear-gradient(90deg,#00d4ff,transparent);}
.kpi-gold::before   {background:linear-gradient(90deg,#f0b429,transparent);}
.kpi-rose::before   {background:linear-gradient(90deg,#ff4d6d,transparent);}
.kpi-green::before  {background:linear-gradient(90deg,#00e5a0,transparent);}
.kpi-icon   {font-size:1.5rem; margin-bottom:0.6rem; display:block;}
.kpi-value  {
    font-family:'Playfair Display',serif !important;
    font-size:2.4rem; font-weight:700;
    color:#e8f4fd; line-height:1;
    margin-bottom:0.3rem; display:block;
}
.kpi-label  {
    font-size:0.72rem; font-weight:600;
    letter-spacing:0.1em; text-transform:uppercase;
    color:#4a7a9b; display:block; margin-bottom:0.15rem;
}
.kpi-sub {
    font-family:'JetBrains Mono',monospace !important;
    font-size:0.68rem; color:#4a7a9b;
}

/* ── INFO BOXES ── */
.info-box {
    background: linear-gradient(135deg,rgba(0,70,120,0.55),rgba(0,40,80,0.55)) !important;
    border: 1px solid rgba(0,212,255,0.2) !important;
    border-left: 3px solid #00d4ff !important;
    border-radius: 12px !important;
    padding: 1.2rem 1.5rem !important;
    margin: 1rem 0 !important;
    color: #e8f4fd !important;
}
.info-box * { color: #e8f4fd !important; }
.info-box strong { color: #00d4ff !important; font-weight:600 !important; }
.info-box em     { color: #a8d8f0 !important; }

.warning-box {
    background: linear-gradient(135deg,rgba(100,60,0,0.55),rgba(70,35,0,0.55)) !important;
    border: 1px solid rgba(240,180,41,0.3) !important;
    border-left: 3px solid #f0b429 !important;
    border-radius: 12px !important;
    padding: 1.2rem 1.5rem !important;
    margin: 1rem 0 !important;
    color: #ffe0a0 !important;
}
.warning-box * { color: #ffe0a0 !important; }
.warning-box strong { color: #f0b429 !important; }

.success-box {
    background: linear-gradient(135deg,rgba(0,80,55,0.55),rgba(0,50,35,0.55)) !important;
    border: 1px solid rgba(0,229,160,0.25) !important;
    border-left: 3px solid #00e5a0 !important;
    border-radius: 12px !important;
    padding: 1.2rem 1.5rem !important;
    margin: 1rem 0 !important;
    color: #a0f0d8 !important;
}
.success-box * { color: #a0f0d8 !important; }
.success-box strong { color: #00e5a0 !important; }

/* ── METRIC WIDGET ── */
[data-testid="stMetric"] {
    background: #071e33 !important;
    border: 1px solid rgba(0,212,255,0.12) !important;
    border-radius: 12px !important;
    padding: 1rem !important;
}
[data-testid="stMetricValue"] {
    font-family: 'Playfair Display', serif !important;
    color: #e8f4fd !important;
    font-size: 1.8rem !important;
}
[data-testid="stMetricLabel"]  { color: #8bafc9 !important; }
[data-testid="stMetricDelta"]  { font-size: 0.85rem !important; }

/* ── TABS ── */
.stTabs [data-baseweb="tab-list"] {
    background: #041428 !important;
    border-radius: 12px !important;
    padding: 4px !important;
    border: 1px solid rgba(0,212,255,0.12) !important;
    gap: 4px !important;
}
.stTabs [data-baseweb="tab"] {
    border-radius: 8px !important;
    color: #8bafc9 !important;
    font-weight: 500 !important;
    font-size: 0.88rem !important;
}
.stTabs [aria-selected="true"] {
    background: linear-gradient(135deg,rgba(0,212,255,0.15),rgba(176,106,255,0.1)) !important;
    color: #00d4ff !important;
    border: 1px solid rgba(0,212,255,0.2) !important;
}

/* ── BUTTONS ── */
.stButton > button {
    background: linear-gradient(135deg,#00d4ff,#0099cc) !important;
    color: #000 !important;
    font-weight: 700 !important;
    border: none !important;
    border-radius: 10px !important;
    letter-spacing: 0.05em !important;
}
.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 25px rgba(0,212,255,0.35) !important;
}

/* ── TEXT AREA ── */
.stTextArea textarea {
    background: #071e33 !important;
    border: 1px solid rgba(0,212,255,0.2) !important;
    border-radius: 10px !important;
    color: #e8f4fd !important;
}

/* ── DATAFRAME ── */
.stDataFrame { border-radius: 12px !important; overflow: hidden !important; }

/* ── SELECTBOX ── */
.stSelectbox > div > div {
    background: #071e33 !important;
    border: 1px solid rgba(0,212,255,0.2) !important;
    border-radius: 10px !important;
    color: #e8f4fd !important;
}

hr { border-color: rgba(0,212,255,0.1) !important; margin: 1.5rem 0 !important; }

.section-title {
    font-family: 'Playfair Display', serif !important;
    font-size: 1.6rem !important;
    font-weight: 700 !important;
    color: #e8f4fd !important;
    margin: 2rem 0 1rem 0 !important;
    display: flex;
    align-item
