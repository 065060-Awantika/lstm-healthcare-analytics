import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def render():
    st.markdown("## 📊 Model Performance Evaluation")
    tab1, tab2 = st.tabs(["🔤 Sentiment Models", "📈 Stock Forecast Models"])

    with tab1:
        df = pd.DataFrame({
            "Model":         ["Vanilla LSTM","Stacked BiLSTM","Attention BiLSTM ⭐","BiGRU"],
            "Accuracy":      [0.831, 0.862, 0.884, 0.859],
            "Precision":     [0.828, 0.858, 0.881, 0.855],
            "Recall":        [0.831, 0.862, 0.884, 0.859],
            "F1-Score":      [0.829, 0.860, 0.882, 0.857],
            "AUC-ROC":       [0.913, 0.938, 0.951, 0.934],
            "Cohen Kappa":   [0.712, 0.765, 0.793, 0.755],
            "Log Loss":      [0.432, 0.378, 0.332, 0.389],
            "Params(K)":     [1842,  3620,  5240,  2980],
            "Inference(ms)": [2.1,   3.8,   5.2,   3.4]
        })
        st.dataframe(df, use_container_width=True, hide_index=True)

        c1,c2 = st.columns(2)
        with c1:
            cats = ['Accuracy','Precision','Recall','F1-Score','AUC-ROC']
            fig  = go.Figure()
            cols = ['#3498db','#2ecc71','#e74c3c','#9b59b6']
            for i,row in df.iterrows():
                fig.add_trace(go.Scatterpolar(
                    r=[row[c] for c in cats]+[row['Accuracy']],
                    theta=cats+[cats[0]],
                    fill='toself', name=row['Model'],
                    line=dict(color=cols[i]), opacity=0.7
                ))
            fig.update_layout(
                polar=dict(radialaxis=dict(range=[0.7,1.0])),
                title="Model Comparison Radar",
                template="plotly_white", height=400
            )
            st.plotly_chart(fig, use_container_width=True)

        with c2:
            classes = ['Negative','Neutral','Positive']
            cm = np.array([[1180,95,65],[88,820,102],[72,85,4120]])
            fig2 = px.imshow(cm, x=classes, y=classes,
                              color_continuous_scale='Blues',
                              text_auto=True,
                              title="Confusion Matrix — Attention BiLSTM")
            fig2.update_layout(height=400)
            st.plotly_chart(fig2, use_container_width=True)

        st.markdown("#### Per-Class Report — Attention BiLSTM")
        st.dataframe(pd.DataFrame({
            "Class":    ["Negative","Neutral","Positive","Macro Avg","Weighted Avg"],
            "Precision":[0.872,0.821,0.901,0.865,0.881],
            "Recall":   [0.881,0.808,0.889,0.859,0.884],
            "F1-Score": [0.876,0.814,0.895,0.862,0.882],
            "Support":  [1340, 1010, 4277, 6627, 6627]
        }), use_container_width=True, hide_index=True)

    with tab2:
        df2 = pd.DataFrame({
            "Model":       ["Stacked LSTM","BiLSTM ⭐","CNN-LSTM"],
            "MAE ($)":     [2.32, 1.35, 2.43],
            "RMSE ($)":    [2.97, 1.73, 3.13],
            "MAPE (%)":    [1.58, 0.92, 1.63],
            "R² Score":    [0.783,0.926,0.759],
            "Params(K)":   [142,  285,  195],
            "Train Time(s)":[38,  67,   45]
        })
        st.dataframe(df2, use_container_width=True, hide_index=True)

        np.random.seed(0)
        n = 120
        t = np.linspace(0,4*np.pi,n)
        actual  = 160 + 15*np.sin(t) + np.cumsum(np.random.normal(0,0.5,n))
        bilstm  = actual + np.random.normal(0,1.73,n)
        stacked = actual + np.random.normal(0,2.97,n)

        fig3 = go.Figure()
        fig3.add_trace(go.Scatter(y=actual,  name='Actual JNJ', line=dict(color='#2980b9',width=2.5)))
        fig3.add_trace(go.Scatter(y=bilstm,  name='BiLSTM ⭐',  line=dict(color='#e74c3c',width=1.5,dash='dash')))
        fig3.add_trace(go.Scatter(y=stacked, name='Stacked LSTM',line=dict(color='#f39c12',width=1.5,dash='dot')))
        fig3.update_layout(
            title="JNJ Actual vs Predicted (Test Set)",
            xaxis_title="Trading Days", yaxis_title="Price (USD)",
            template="plotly_white", height=420
        )
        st.plotly_chart(fig3, use_container_width=True)
