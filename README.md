# 🏥 LSTM Healthcare Analytics Dashboard

> **Project 4 Capstone** | Deep Learning for Business Decision-Making  
> Personal Care & Wellness Sentiment × Johnson & Johnson (JNJ) Stock Forecasting

Streamlit LINK - https://lstm-healthcare-analytics-ikmfzpaunqj6wwwz8mqt2v.streamlit.app/

---

## 📌 Overview

This project applies **Long Short-Term Memory (LSTM)** deep learning models to the healthcare domain — specifically Personal Care & Wellness — to derive actionable business intelligence from two data sources:

| Data Source | Type | Purpose |
|-------------|------|---------|
| Amazon Product Reviews (Personal Care) | Text / NLP | Sentiment Classification |
| Johnson & Johnson (JNJ) Stock Prices 2015–2024 | Time Series | Price Forecasting |

The goal is to demonstrate how **consumer sentiment** and **stock price trends** can be jointly modeled to support proactive business decisions in marketing, R&D, finance, and supply chain.

---

## 🎯 Competency Goals

| Goal | Description |
|------|-------------|
| **CG1** | Apply deep learning models to real-world business problems |
| **CG2** | Preprocess and engineer features from text and time-series data |
| **CG3** | Evaluate model performance using industry-standard metrics |
| **CG6** | Communicate ethical considerations in AI/ML deployments |

---

## 🧠 Models Built

### Text Sentiment Classification (4 Models)
| Model | F1-Score | AUC-ROC | Params |
|-------|----------|---------|--------|
| Vanilla LSTM | 0.831 | 0.913 | 184K |
| Stacked BiLSTM | 0.860 | 0.938 | 362K |
| **Attention BiLSTM ⭐ Best** | **0.884** | **0.951** | 524K |
| Bidirectional GRU | 0.857 | 0.934 | 298K |

### Stock Price Forecasting (3 Models)
| Model | MAE | RMSE | R² Score |
|-------|-----|------|----------|
| Stacked LSTM | $2.32 | $2.97 | 0.783 |
| **BiLSTM ⭐ Best** | **$1.35** | **$1.73** | **0.926** |
| CNN-LSTM Hybrid | $2.43 | $3.13 | 0.759 |

---

## 📊 Dashboard Pages

### 🏠 Home
- Live KPI metrics (F1, R², RMSE, dataset size)
- Project problem statement and objectives
- Live JNJ candlestick chart via Yahoo Finance
- Full model architecture summary table

### 📈 JNJ Stock Forecast
- CNN-LSTM multivariate forecast with 12 features
- Configurable forecast horizon (5–60 days)
- RSI and MACD technical indicators
- Trading signals (Bullish / Bearish / Neutral)
- 95% confidence interval bands

### 💡 Business Recommendations
- Real-time sentiment analyzer for product reviews
- Automated department action triggers
- Decision policy matrix (6 key business signals)
- Sentiment vs JNJ stock correlation trend chart

### 📊 Model Performance
- Radar chart comparison across all 4 text models
- Confusion matrix for best text model
- ROC curves and per-class classification report
- Time series actual vs predicted plots

### ⚖️ Ethics & Responsibility
- Data legitimacy and consent documentation
- PII anonymization pipeline (names, emails, phones)
- Gender and racial bias audit results
- LIME and SHAP explainability analysis

---

## 🗂️ Repository Structure

```
lstm-healthcare-analytics/
│
├── app.py                          # Main Streamlit application
├── requirements.txt                # Python dependencies
├── README.md                       # This file
│
└── pages/
    ├── home.py                     # Home page
    ├── forecast.py                 # Stock forecast page
    ├── recommendations.py          # Business recommendations
    ├── performance.py              # Model performance metrics
    └── ethics.py                   # Ethics and responsibility
```

---

## ⚙️ Tech Stack

| Category | Tools |
|----------|-------|
| Deep Learning | TensorFlow 2.19, Keras |
| NLP | NLTK, VADER, LIME, SHAP |
| Data | yfinance, pandas, numpy |
| Visualization | Plotly, Matplotlib, Seaborn |
| App Framework | Streamlit |
| Model Architectures | LSTM, BiLSTM, GRU, CNN-LSTM, Attention |

---

## 🚀 Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/lstm-healthcare-analytics.git
cd lstm-healthcare-analytics

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
streamlit run app.py
```

---

## 📦 Data Sources

| Source | Description | License |
|--------|-------------|---------|
| [Amazon Reviews 2023](https://huggingface.co/datasets/McAuley-Lab/Amazon-Reviews-2023) | Personal Care & Wellness product reviews | Amazon Public Dataset License |
| [Yahoo Finance / yfinance](https://pypi.org/project/yfinance/) | JNJ stock prices 2015–2024 | Public market data |

> ⚠️ All data used strictly for **academic research purposes only**. No commercial use. No redistribution.

---

## 🔒 Ethical Considerations

- ✅ **PII Anonymization**: All names, emails, phone numbers masked using regex pipeline
- ✅ **Bias Audit**: Gender term frequency analysis performed; class-weighted training applied
- ✅ **Explainability**: LIME and SHAP used to validate model logic
- ✅ **Data Consent**: Only publicly available, licensed datasets used
- ✅ **No Commercial Use**: Strictly academic capstone project

---

## 📈 Key Business Insights

1. **Negative sentiment spikes** are a ~2-week leading indicator before JNJ stock price dips
2. **BiLSTM** outperforms all other architectures for stock forecasting (R² = 0.926)
3. **Attention mechanism** improves sentiment classification F1 by 5.3% over vanilla LSTM
4. **Safety-related terms** (allergic, rash) have highest SHAP importance — model correctly prioritizes risk signals
5. **Class-weighted training** improved minority class (Neutral) F1 by 11.3 percentage points

---

## 👩‍💻 Author

**Capstone Project — Project 4**  
Healthcare Domain | Personal Care & Wellness  
Deep Learning & NLP | Business Intelligence

---

## 📄 License

This project is submitted as part of an **academic capstone** requirement.  
All code is original. Data sources are publicly licensed.  
Not intended for commercial use.
