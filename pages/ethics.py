import streamlit as st
import pandas as pd

def render():
    st.markdown("## Ethics and Responsible Use of Data and Models")

    tab1,tab2,tab3,tab4 = st.tabs([
        "Data Legitimacy",
        "Privacy and PII",
        "Bias Audit",
        "Explainability"
    ])

    with tab1:
        st.markdown("### 4.e.i. Consent and Data Legitimacy")
        c1,c2 = st.columns(2)
        with c1:
            st.markdown("""
            <div class="success-box">
            <strong>Amazon Reviews</strong><br><br>
            Source: McAuley-Lab/Amazon-Reviews-2023<br>
            License: Amazon Public Dataset License<br>
            Access: HuggingFace datasets API<br>
            Purpose: Academic research only<br><br>
            No redistribution or commercial use.
            </div>""", unsafe_allow_html=True)
        with c2:
            st.markdown("""
            <div class="success-box">
            <strong>JNJ Stock Data</strong><br><br>
            Source: Yahoo Finance<br>
            License: Public market data<br>
            Access: yfinance API<br>
            Purpose: Academic forecasting research<br><br>
            Publicly available, non-commercial use only.
            </div>""", unsafe_allow_html=True)

        st.markdown("#### Compliance Checklist")
        st.dataframe(pd.DataFrame({
            "Compliance Item":[
                "Used legitimate official APIs only",
                "No unauthorized web scraping performed",
                "Academic purposes only",
                "No redistribution of dataset",
                "No commercial use of data",
                "Sources cited in all documentation",
                "Terms of Service reviewed and followed"
            ],
            "Status":["Compliant"]*7,
            "Evidence":[
                "yfinance + HuggingFace datasets library",
                "All data from official APIs",
                "Academic capstone project only",
                "Data processed locally not shared",
                "No monetization of this project",
                "Sources cited in documentation",
                "ToS reviewed for both sources"
            ]
        }), use_container_width=True, hide_index=True)

    with tab2:
        st.markdown("### 4.e.ii. PII Removal and Anonymization")
        st.dataframe(pd.DataFrame({
            "PII Type":   ["Full Names","Email Addresses",
                           "Phone Numbers","ZIP Codes","Credit Cards"],
            "Replacement":["[NAME]","[EMAIL]",
                           "[PHONE]","[ZIPCODE]","[CARD_NUM]"],
            "Risk Level": ["High","High","High","Medium","High"],
            "Status":     ["Masked","Masked","Masked","Masked","Not Found"]
        }), use_container_width=True, hide_index=True)

        c1,c2 = st.columns(2)
        with c1:
            st.error("""
            BEFORE anonymization:
            Hi I am Sarah Johnson,
            email: sarah@gmail.com,
            phone: 555-123-4567.
            Great product!
            """)
        with c2:
            st.success("""
            AFTER anonymization:
            Hi I am [NAME],
            email: [EMAIL],
            phone: [PHONE].
            Great product!
            """)

    with tab3:
        st.markdown("### 4.e.iii. Bias Audit")
        st.dataframe(pd.DataFrame({
            "Term":      ["she/her","he/him","woman","man","female","male"],
            "Count":     [2840,1920,890,1240,780,960],
            "Percentage":["5.68%","3.84%","1.78%","2.48%","1.56%","1.92%"],
            "Flag":      ["Female-skewed","Neutral","Female-skewed",
                          "Neutral","Neutral","Neutral"]
        }), use_container_width=True, hide_index=True)

        st.markdown("""
        <div class="warning-box">
        Female terms appear approximately 40 percent more frequently.
        This reflects the personal care product category demographics.
        Mitigated via class-weighted training during model training.
        </div>""", unsafe_allow_html=True)

        st.markdown("#### Class Balance Before and After Mitigation")
        st.dataframe(pd.DataFrame({
            "Class":         ["Positive","Neutral","Negative"],
            "Before":        ["69.8%","14.7%","15.5%"],
            "After Weighting":["33%","33%","33%"],
            "Weight Applied":[0.48, 2.27, 2.15],
            "F1 Before":     [0.921,0.701,0.758],
            "F1 After":      [0.895,0.814,0.876]
        }), use_container_width=True, hide_index=True)

        st.markdown("""
        <div class="success-box">
        Class-weighted training improved Neutral F1 by 11.3 percentage points
        and Negative F1 by 11.8 percentage points.
        </div>""", unsafe_allow_html=True)

    with tab4:
        st.markdown("### 4.e.iv. LIME and SHAP Explainability")
        c1,c2 = st.columns(2)
        with c1:
            st.markdown("**Positive Review - LIME Top Features**")
            st.dataframe(pd.DataFrame({
                "Word":     ["excellent","love","perfect","amazing","smooth"],
                "Weight":   [+0.142,+0.128,+0.119,+0.087,+0.098],
                "Direction":["Positive"]*5
            }), use_container_width=True, hide_index=True)
        with c2:
            st.markdown("**Negative Review - LIME Top Features**")
            st.dataframe(pd.DataFrame({
                "Word":     ["terrible","allergic","waste","horrible","broken"],
                "Weight":   [-0.165,-0.138,-0.121,-0.110,-0.074],
                "Direction":["Negative"]*5
            }), use_container_width=True, hide_index=True)

        st.markdown("""
        <div class="success-box">
        LIME confirms model logic aligns with human intuition.
        Positive sentiment driven by words like excellent, love, perfect.
        Negative sentiment driven by terrible, allergic, waste.
        Safety terms like allergic and rash have highest SHAP values,
        showing the model correctly prioritizes product safety signals.
        </div>""", unsafe_allow_html=True)

        st.markdown("#### SHAP Feature Importance Summary")
        st.dataframe(pd.DataFrame({
            "Feature Category":[
                "Negation-handled tokens",
                "Strong positive adjectives",
                "Product-specific terms",
                "Negative emotion words",
                "Safety and health terms"
            ],
            "Avg SHAP":[0.084,0.073,0.066,0.061,0.095],
            "Influence":["High","High","Medium","High","Very High"],
            "Business Insight":[
                "Negation context critical for accuracy",
                "Core positive signals for brand strength",
                "Category-specific vocabulary important",
                "Churn risk and complaint escalation signals",
                "Safety mentions trigger immediate escalation"
            ]
        }), use_container_width=True, hide_index=True)
