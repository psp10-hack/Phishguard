import joblib
import pandas as pd

from feature_extractor import extract_features


# Load trained model
model = joblib.load("models/phishguard_model.pkl")


# Ask for URL
url = input("Enter URL: ")


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


# Display extracted features
print("\n========== URL FEATURES ==========")

for name, value in zip(feature_names, features):
    print(f"{name:15}: {value}")


# Convert features into DataFrame
X = pd.DataFrame(
    [features],
    columns=feature_names
)


# Prediction
prediction = model.predict(X)[0]

# Prediction probability
probability = model.predict_proba(X)[0]


# Display result
print("\n========== PHISHGUARD RESULT ==========")

if prediction == 1:
    print("Prediction : PHISHING")
    print("Confidence :",
          round(probability[1] * 100, 2), "%")
else:
    print("Prediction : BENIGN")
    print("Confidence :",
          round(probability[0] * 100, 2), "%")