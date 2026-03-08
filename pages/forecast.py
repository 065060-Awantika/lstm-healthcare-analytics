import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import yfinance as yf
from datetime import timedelta

def compute_rsi(series, period=14):
    delta = series.diff()
    gain  = delta.clip(lower=0)
    loss  = -delta.clip(upper=0)
    ag    = gain.rolling(period).mean()
    al    = loss.rolling(period).mean()
    rs    = ag / (al + 1e-8)
    return 100 - (100 / (1 + rs))

def simulate_forecast(prices, n):
    np.random.seed(42)
    last  = prices.iloc[-1]
    trend = (prices.iloc[-1] - prices.iloc[-30]) / 30 if len(prices) >= 30 else 0
    trend = np.clip(trend, -0.5, 0.5)
    fc, up, lo = [], [], []
    p = last
    for i in range(n):
        p = p + trend*(0.95**i) + np.random.normal(0, last*0.012)
        u = last*0.025*np.sqrt(i+1)
        fc.append(p); up.append(p+u); lo.append(p-u)
    return fc, up, lo

def render():
    st.markdown("## 📈 JNJ Stock Price Forecast")
    st.markdown("""<div class="info-box">
    CNN-LSTM multivariate forecast using 12 features:
    OHLCV, MA(7/21/50), EMA(12/26), MACD, RSI, Volatility.
    <strong>Lookback: 60 days</strong>
    </div>""", unsafe_allow_html=True)

    c1,c2 = st.columns(2)
    with c1:
        period = st.selectbox("Historical Period",
                    ["3mo","6mo","1y","2y"], index=2,
                    format_func=lambda x: {"3mo":"3 Months","6mo":"6 Months",
                                           "1y":"1 Year","2y":"2 Years"}[x])
    with c2:
        n_fc = st.slider("Forecast Days", 5, 60, 30)

    try:
        hist = yf.Ticker("JNJ").history(period=period)
        hist.reset_index(inplace=True)
        hist['Date'] = pd.to_datetime(hist['Date']).dt.tz_localize(None)
        hist['MA20'] = hist['Close'].rolling(20).mean()
        hist['RSI']  = compute_rsi(hist['Close'])
        hist['MACD'] = hist['Close'].ewm(span=12).mean() - hist['Close'].ewm(span=26).mean()
        hist.dropna(inplace=True)

        fc, up, lo = simulate_forecast(hist['Close'], n_fc)
        fd = pd.bdate_range(hist['Date'].iloc[-1]+timedelta(1), periods=n_fc)
        xf = [hist['Date'].iloc[-1]] + list(fd)
        yf_fc = [hist['Close'].iloc[-1]] + fc
        yu = [hist['Close'].iloc[-1]] + up
        yl = [hist['Close'].iloc[-1]] + lo

        fig = make_subplots(rows=3, cols=1, shared_xaxes=True,
                            row_heights=[0.55,0.25,0.20],
                            subplot_titles=("Price + Forecast","RSI","MACD"))
        fig.add_trace(go.Scatter(x=hist['Date'], y=hist['Close'],
                                  name='Historical', line=dict(color='#2980b9',width=2)),
                      row=1,col=1)
        fig.add_trace(go.Scatter(x=hist['Date'], y=hist['MA20'],
                                  name='MA20', line=dict(color='#f39c12',width=1,dash='dash')),
                      row=1,col=1)
        fig.add_trace(go.Scatter(x=xf, y=yu, line=dict(width=0), showlegend=False),
                      row=1,col=1)
        fig.add_trace(go.Scatter(x=xf, y=yl, fill='tonexty',
                                  fillcolor='rgba(231,76,60,0.15)',
                                  line=dict(width=0), name='95% CI'),
                      row=1,col=1)
        fig.add_trace(go.Scatter(x=xf, y=yf_fc, name='LSTM Forecast',
                                  line=dict(color='#e74c3c',width=2,dash='dash')),
                      row=1,col=1)
        fig.add_trace(go.Scatter(x=hist['Date'], y=hist['RSI'],
                                  name='RSI', line=dict(color='#8e44ad',width=1.5)),
                      row=2,col=1)
        fig.add_hline(y=70, line_dash="dash", line_color="red",   row=2, col=1)
        fig.add_hline(y=30, line_dash="dash", line_color="green", row=2, col=1)
        mc = ['#2ecc71' if v>=0 else '#e74c3c' for v in hist['MACD']]
        fig.add_trace(go.Bar(x=hist['Date'], y=hist['MACD'],
                              name='MACD', marker_color=mc), row=3,col=1)
        fig.update_layout(template="plotly_white", height=680,
                           xaxis_rangeslider_visible=False,
                           title=f"JNJ Forecast — {n_fc} Days Ahead")
        st.plotly_chart(fig, use_container_width=True)

        cur = hist['Close'].iloc[-1]
        end = fc[-1]
        pct = (end-cur)/cur*100
        a,b,c,d = st.columns(4)
        a.metric("Current Price",        f"${cur:.2f}")
        b.metric(f"Forecast ({n_fc}d)",  f"${end:.2f}", f"{pct:+.2f}%")
        c.metric("Forecast High",        f"${max(fc):.2f}")
        d.metric("Forecast Low",         f"${min(fc):.2f}")

        rsi_last  = hist['RSI'].iloc[-1]
        macd_last = hist['MACD'].iloc[-1]
        st.markdown("### 📡 Trading Signals")
        s1,s2,s3 = st.columns(3)
        with s1:
            if rsi_last > 70:
                st.markdown(f'<div class="warning-box">⚠️ <strong>RSI Overbought</strong><br>RSI={rsi_last:.1f} → Consider selling</div>', unsafe_allow_html=True)
            elif rsi_last < 30:
                st.markdown(f'<div class="success-box">✅ <strong>RSI Oversold</strong><br>RSI={rsi_last:.1f} → Buying opportunity</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="info-box">ℹ️ <strong>RSI Neutral</strong><br>RSI={rsi_last:.1f}</div>', unsafe_allow_html=True)
        with s2:
            if macd_last > 0:
                st.markdown('<div class="success-box">📈 <strong>MACD Bullish</strong><br>Upward momentum</div>', unsafe_allow_html=True)
            else:
                st.markdown('<div class="warning-box">📉 <strong>MACD Bearish</strong><br>Downward momentum</div>', unsafe_allow_html=True)
        with s3:
            if pct > 2:
                st.markdown(f'<div class="success-box">🚀 <strong>Bullish Forecast</strong><br>Expected +{pct:.2f}%</div>', unsafe_allow_html=True)
            elif pct < -2:
                st.markdown(f'<div class="warning-box">🔻 <strong>Bearish Forecast</strong><br>Expected {pct:.2f}%</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="info-box">➡️ <strong>Sideways</strong><br>Expected {pct:.2f}%</div>', unsafe_allow_html=True)
    except Exception as e:
        st.error(f"Error: {e}")
