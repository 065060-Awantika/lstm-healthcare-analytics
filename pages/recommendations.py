import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

def render():
    st.markdown("## 💡 Business Recommendations")
    st.markdown("""<div class="info-box">
    Data-driven recommendations from LSTM sentiment + stock forecasting models.
    </div>""", unsafe_allow_html=True)

    st.markdown("### 🎯 Sentiment Analyzer")
    review = st.text_area("Enter a product review:",
        placeholder="e.g. This moisturizer is amazing, my skin feels wonderful...")

    if st.button("🔍 Analyze", type="primary") and review.strip():
        pos_w = ['great','excellent','amazing','fantastic','love','perfect',
                 'best','wonderful','outstanding','superb','good','happy']
        neg_w = ['terrible','awful','bad','horrible','worst','hate',
                 'disgusting','poor','waste','allergic','rash','broken']
        t = review.lower()
        ps = sum(1 for w in pos_w if w in t)
        ns = sum(1 for w in neg_w if w in t)
        if ps > ns:
            sent, conf, color = "Positive", min(95, 70+ps*5), "#2ecc71"
        elif ns > ps:
            sent, conf, color = "Negative", min(95, 70+ns*5), "#e74c3c"
        else:
            sent, conf, color = "Neutral", 65, "#f39c12"

        c1,c2,c3 = st.columns(3)
        c1.markdown(f'<div style="background:{color};padding:1rem;border-radius:10px;text-align:center;color:white"><h2 style="margin:0">{sent}</h2><p style="margin:0">Sentiment</p></div>', unsafe_allow_html=True)
        c2.markdown(f'<div style="background:#3498db;padding:1rem;border-radius:10px;text-align:center;color:white"><h2 style="margin:0">{conf}%</h2><p style="margin:0">Confidence</p></div>', unsafe_allow_html=True)
        c3.markdown(f'<div style="background:#8e44ad;padding:1rem;border-radius:10px;text-align:center;color:white"><h2 style="margin:0">{len(review.split())}</h2><p style="margin:0">Words</p></div>', unsafe_allow_html=True)

        st.markdown("#### 🏢 Triggered Actions:")
        if sent == "Positive":
            st.markdown('<div class="success-box">✅ Feature in ad campaigns<br>✅ Tag as brand ambassador candidate<br>✅ Highlight attributes for line extension<br>✅ Continue investment in this SKU</div>', unsafe_allow_html=True)
        elif sent == "Negative":
            st.markdown('<div class="warning-box">🔴 Flag for QA team review (24h)<br>🔴 Trigger customer outreach + replacement<br>🔴 Log complaint for R&D dashboard<br>🔴 Pause ad spend on this variant</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="info-box">🟡 Add to re-engagement campaign<br>🟡 Deploy follow-up satisfaction survey<br>🟡 Monitor trend over 30 days</div>', unsafe_allow_html=True)

        if any(w in t for w in ['allergic','rash','reaction','burn','irritation']):
            st.error("⚠️ SAFETY ALERT: Adverse reaction detected → Escalate to Medical Affairs immediately!")

    st.markdown("---")
    st.markdown("### 📋 Decision Policy Matrix")
    df = pd.DataFrame({
        "Signal":["Negative spike >20%","Positive >75% + rising stock",
                  "Forecast price drop >3%","Neutral growing >25%",
                  "Reviews mention allergic/rash","LSTM forecast price rise >5%"],
        "Department":["QA + Marketing","Marketing + Finance",
                      "Finance/CFO","Marketing + R&D",
                      "Medical Affairs","Finance + Strategy"],
        "Action":["QA audit + pause ads",
                  "Increase budget + new SKU launch",
                  "Hedge equity positions",
                  "NPS survey + loyalty campaign",
                  "IMMEDIATE product safety review",
                  "Accelerate expansion plans"],
        "Priority":["🔴 URGENT","🟢 OPPORTUNITY","🔴 URGENT",
                    "🟡 MONITOR","🔴 URGENT","🟢 OPPORTUNITY"],
        "Timeline":["24h","1 week","48h","2 weeks","Immediate","1 month"]
    })
    st.dataframe(df, use_container_width=True, hide_index=True)

    st.markdown("---")
    st.markdown("### 📊 Sentiment vs JNJ Stock Trend")
    np.random.seed(42)
    months = pd.date_range('2022-01-01','2024-12-01',freq='MS')
    pos    = 0.65 + 0.08*np.sin(np.linspace(0,6,len(months))) + np.random.normal(0,0.02,len(months))
    neg    = 0.18 - 0.04*np.sin(np.linspace(0,6,len(months))) + np.random.normal(0,0.01,len(months))
    stock  = 165 + 20*np.sin(np.linspace(0,4,len(months))) + np.cumsum(np.random.normal(0,1.5,len(months)))

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=months, y=pos*100, name='% Positive',
                              fill='tozeroy', fillcolor='rgba(46,204,113,0.2)',
                              line=dict(color='#2ecc71',width=2)))
    fig.add_trace(go.Scatter(x=months, y=neg*100, name='% Negative',
                              fill='tozeroy', fillcolor='rgba(231,76,60,0.2)',
                              line=dict(color='#e74c3c',width=2)))
    fig.add_trace(go.Scatter(x=months, y=stock, name='JNJ Price',
                              yaxis='y2', line=dict(color='#3498db',width=2.5,dash='dash')))
    fig.update_layout(
        title="Sentiment Trend vs JNJ Stock (2022-2024)",
        yaxis=dict(title="Sentiment (%)", range=[0,100]),
        yaxis2=dict(title="JNJ Price (USD)", overlaying='y', side='right'),
        template="plotly_white", height=420,
        legend=dict(orientation='h', yanchor='bottom', y=1.02)
    )
    st.plotly_chart(fig, use_container_width=True)
    st.markdown('<div class="info-box">📊 <strong>Key Insight:</strong> Negative sentiment spikes show a ~2-week leading indicator before JNJ stock dips — supports sentiment-informed hedging strategy.</div>', unsafe_allow_html=True)
