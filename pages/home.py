import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import yfinance as yf

def render():
    col1,col2,col3,col4 = st.columns(4)
    metrics = [
        ("Sentiment F1","88.4%","Attention BiLSTM"),
        ("Stock R2","92.6%","BiLSTM Model"),
        ("Stock RMSE","$1.73","Forecast Error"),
        ("Reviews Analyzed","50,000","Amazon Dataset"),
    ]
    for col,(label,value,sub) in zip([col1,col2,col3,col4],metrics):
        col.markdown(f"""
        <div class="metric-card">
            <h3>{value}</h3>
            <p>{label}</p>
            <p style="font-size:0.75rem;opacity:0.7">{sub}</p>
        </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### Problem Statement")
    st.markdown("""
    <div class="info-box">
    <strong>Research Question:</strong><br>
    Can consumer sentiment from Amazon Personal Care and Wellness reviews,
    combined with JNJ stock price patterns, be leveraged through LSTM models
    to support proactive business decisions around product strategy,
    marketing allocation, and investment risk management?
    </div>""", unsafe_allow_html=True)

    c1,c2 = st.columns(2)
    with c1:
        st.markdown("**Objectives**")
        st.markdown("""
        1. Multi-class LSTM sentiment classifier (Positive / Neutral / Negative)
        2. Multivariate LSTM stock price forecasting for JNJ
        3. Sentiment-stock correlation for business insights
        """)
    with c2:
        st.markdown("**Business Value**")
        st.markdown("""
        - Marketing: Sentiment alerts trigger targeted campaigns
        - R&D: Pain points guide product improvements
        - Finance: Sentiment informs hedging strategies
        - Supply Chain: Demand signal from reviews
        """)

    st.markdown("---")
    st.markdown("### Live JNJ Stock")
    try:
        jnj  = yf.Ticker("JNJ")
        hist = jnj.history(period="3mo")
        hist.reset_index(inplace=True)
        hist['Date'] = pd.to_datetime(hist['Date']).dt.tz_localize(None)

        fig = go.Figure()
        fig.add_trace(go.Candlestick(
            x=hist['Date'],
            open=hist['Open'], high=hist['High'],
            low=hist['Low'],   close=hist['Close'],
            name='JNJ',
            increasing_line_color='#2ecc71',
            decreasing_line_color='#e74c3c'
        ))
        fig.update_layout(
            title="JNJ Last 3 Months",
            template="plotly_white",
            height=400,
            xaxis_rangeslider_visible=False
        )
        st.plotly_chart(fig, use_container_width=True)

        latest = hist.iloc[-1]
        prev   = hist.iloc[-2]
        chg    = latest['Close'] - prev['Close']
        pct    = chg / prev['Close'] * 100
        a,b,c,d = st.columns(4)
        a.metric("Last Close", f"${latest['Close']:.2f}", f"{chg:+.2f} ({pct:+.2f}%)")
        b.metric("Day High",   f"${latest['High']:.2f}")
        c.metric("Day Low",    f"${latest['Low']:.2f}")
        d.metric("Volume",     f"{latest['Volume']/1e6:.1f}M")
    except Exception as e:
        st.warning(f"Live data unavailable: {e}")

    st.markdown("---")
    st.markdown("### Model Summary")
    df = pd.DataFrame({
        "Model":["Vanilla LSTM","Stacked BiLSTM","Attention BiLSTM (Best)","BiGRU",
                 "Stacked LSTM (Stock)","BiLSTM (Stock - Best)","CNN-LSTM (Stock)"],
        "Task": ["Sentiment","Sentiment","Sentiment","Sentiment",
                 "Forecast","Forecast","Forecast"],
        "Key Metric":["F1=0.831","F1=0.860","F1=0.884","F1=0.857",
                      "R2=0.783","R2=0.926","R2=0.759"]
    })
    st.dataframe(df, use_container_width=True, hide_index=True)
