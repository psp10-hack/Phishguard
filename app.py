import streamlit as st
import joblib
import pandas as pd

from modules.feature_extractor import (
    extract_features,
    get_risk_factors
)


# Load trained model
model = joblib.load("models/phishguard_model.pkl")


# Page settings
st.set_page_config(
    page_title="PhishGuard",
    page_icon="🛡️",
    layout="centered"
)


# Title
st.title("🛡️ PhishGuard")
st.subheader("AI-Powered Phishing URL Detector")

st.write(
    "Enter a URL below and PhishGuard will analyze its "
    "characteristics and predict whether it is benign or phishing."
)


# URL input
url = st.text_input(
    "Enter URL",
    placeholder="https://example.com/login"
)


# Scan button
if st.button("🔍 Scan URL"):

    if not url:

        st.warning("Please enter a URL.")

    else:

        # Extract features
        features = extract_features(url)

        # Feature names
        feature_names = [
            "url_len",
            "dom_len",
            "is_ip",
            "tld_len",
            "subdom_cnt",
            "letter_cnt",
            "digit_cnt",
            "special_cnt",
            "eq_cnt",
            "qm_cnt",
            "amp_cnt",
            "dot_cnt",
            "dash_cnt",
            "under_cnt",
            "letter_ratio",
            "digit_ratio",
            "spec_ratio",
            "is_https",
            "slash_cnt",
            "entropy",
            "path_len",
            "query_len"
        ]

        # Convert features into DataFrame
        X = pd.DataFrame(
            [features],
            columns=feature_names
        )

        # Make prediction
        prediction = model.predict(X)[0]

        # Get probabilities
        probability = model.predict_proba(X)[0]

        # Phishing probability
        phishing_probability = probability[1] * 100


        # =========================
        # RESULT
        # =========================

        st.divider()

        st.subheader("PhishGuard Result")


        if phishing_probability >= 70:

            st.error(
                "🚨 HIGH RISK: PHISHING URL"
            )

        elif phishing_probability >= 30:

            st.warning(
                "⚠️ MEDIUM RISK"
            )

        else:

            st.success(
                "✅ LOW RISK: BENIGN URL"
            )


        st.metric(
            "Phishing Probability",
            f"{phishing_probability:.2f}%"
        )


        # =========================
        # RISK FACTORS
        # =========================

        risk_factors = get_risk_factors(
            url,
            features
        )

        st.divider()

        st.subheader("⚠️ Risk Factors")


        if risk_factors:

            for factor in risk_factors:

                st.write(
                    "⚠️",
                    factor
                )

        else:

            st.write(
                "✅ No major suspicious URL characteristics detected."
            )


        # =========================
        # URL FEATURES
        # =========================

        st.divider()

        st.subheader("📊 URL Features")


        feature_data = {
            name: value
            for name, value in zip(
                feature_names,
                features
            )
        }


        st.dataframe(
            pd.DataFrame(
                feature_data.items(),
                columns=[
                    "Feature",
                    "Value"
                ]
            ),
            use_container_width=True
        )