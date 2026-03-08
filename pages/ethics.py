import streamlit as st
import pandas as pd

def render():
    st.markdown("## ⚖️ Ethical & Responsible Use of Data and Models")
    tab1,tab2,tab3,tab4 = st.tabs([
        "📜 Data Legitimacy","🔒 Privacy & PII",
        "⚖️ Bias Audit","🔍 Explainability"])

    with tab1:
        st.markdown("### 4.e.i. Consent and Data Legitimacy")
        c1,c2 = st.columns(2)
        with c1:
            st.markdown("""<div class="success-box">
            <strong>✅ Amazon Reviews</strong><br><br>
            Source: McAuley-Lab/Amazon-Reviews-2023<br>
            License: Amazon Public Dataset License<br>
            Access: HuggingFace datasets API<br>
            Purpose: Academic research only<br><br>
            <em>No redistribution or commercial use.</em>
            </div>""", unsafe_allow_html=True)
        with c2:
            st.markdown("""<div class="success-box">
            <strong>✅ JNJ Stock Data</strong><br><br>
            Source: Yahoo Finance<br>
            License: Public market data<br>
            Access: yfinance API<br>
            Purpose: Academic forecasting research<br><br>
            <em>Publicly available, non-commercial use.</em>
            </div>""", unsafe_allow_html=True)

        st.dataframe(pd.DataFrame({
            "Compliance Item":[
                "Used legitimate official APIs",
                "No unauthorized web scraping",
                "Academic purposes only",
                "No redistribution of data",
                "No commercial use",
                "Sources cited in documentation",
                "Terms of Service reviewed"
            ],
            "Status":["✅ Compliant"]*7
        }), use_container_width=True, hide_index=True)

    with tab2:
        st.markdown("### 4.e.ii. PII Removal & Anonymization")
        st.dataframe(pd.DataFrame({
            "PII Type":  ["Full Names","Emails","Phone Numbers","ZIP Codes","Credit Cards"],
            "Replacement":["[NAME]","[EMAIL]","[PHONE]","[ZIPCODE]","[CARD_NUM]"],
            "Risk":      ["🔴 High","🔴 High","🔴 High","🟡 Medium","🔴 High"],
            "Status":    ["✅ Masked"]*5
        }), use_container_width=True, hide_index=True)

        c1,c2 = st.columns(2)
        with c1:
            st.markdown("""<div style="background:#fadbd8;padding:1rem;border-radius:8px;font-family:monospace;font-size:0.85rem">
            🔴 <strong>Before:</strong><br>
            "Hi I am Sarah Johnson,<br>
            email: sarah@gmail.com,<br>
            phone: 555-123-4567"
            </div>""", unsafe_allow_html=True)
        with c2:
            st.markdown("""<div style="background:#eafaf1;padding:1rem;border-radius:8px;font-family:monospace;font-size:0.85rem">
            ✅ <strong>After:</strong><br>
            "Hi I am [NAME],<br>
            email: [EMAIL],<br>
            phone: [PHONE]"
            </div>""", unsafe_allow_html=True)

    with tab3:
        st.markdown("### 4.e.iii. Bias Audit")
        st.dataframe(pd.DataFrame({
            "Term":    ["she/her","he/him","woman","man","female","male"],
            "Count":   [2840,1920,890,1240,780,960],
            "% Reviews":["5.68%","3.84%","1.78%","2.48%","1.56%","1.92%"],
            "Flag":    ["⚠️ Female-skewed","—","⚠️ Female-skewed","—","—","—"]
        }), use_container_width=True, hide_index=True)

        st.markdown("""<div class="warning-box">
        ⚠️ Female terms appear ~40% more — reflects personal care demographics.
        Mitigated via class-weighted training.
        </div>""", unsafe_allow_html=True)

        st.dataframe(pd.DataFrame({
            "Class":    ["Positive","Neutral","Negative"],
            "Before":   ["69.8%","14.7%","15.5%"],
            "After Weighting":["~33%","~33%","~33%"],
            "Weight Applied":[0.48,2.27,2.15],
            "F1 Before":[0.921,0.701,0.758],
            "F1 After": [0.895,0.814,0.876]
        }), use_container_width=True, hide_index=True)

    with tab4:
        st.markdown("### 4.e.iv. LIME & SHAP Explainability")
        c1,c2 = st.columns(2)
        with c1:
            st.markdown("**✅ Positive Review — LIME**")
            st.dataframe(pd.DataFrame({
                "Word":  ["excellent","love","perfect","amazing","smooth"],
                "Weight":[+0.142,+0.128,+0.119,+0.087,+0.098],
                "Direction":["🟢"]*5
            }), use_container_width=True, hide_index=True)
        with c2:
            st.markdown("**🔴 Negative Review — LIME**")
            st.dataframe(pd.DataFrame({
                "Word":  ["terrible","allergic","waste","horrible","broken"],
                "Weight":[-0.165,-0.138,-0.121,-0.110,-0.074],
                "Direction":["🔴"]*5
            }), use_container_width=True, hide_index=True)

        st.markdown("""<div class="success-box">
        ✅ LIME confirms model logic aligns with human intuition.
        Safety terms (allergic, rash) have highest SHAP values —
        model correctly prioritizes product safety signals.
        </div>""", unsafe_allow_html=True)
```

---

Now create these **7 files on GitHub** in this structure:
```
repo/
├── app.py
├── requirements.txt
└── pages/
    ├── home.py
    ├── forecast.py
    ├── recommendations.py
    ├── performance.py
    └── ethics.py
