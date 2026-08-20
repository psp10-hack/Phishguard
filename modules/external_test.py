import joblib
import pandas as pd

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

from feature_extractor import extract_features


# Load trained model
model = joblib.load("models/phishguard_model.pkl")


# =========================
# LOAD EXTERNAL DATASETS
# =========================

phishing_df = pd.read_csv(
    "data/phishing_10000.csv"
)

benign_df = pd.read_csv(
    "data/benign_10000.csv"
)


# Get URLs
phishing_urls = (
    phishing_df["url"]
    .dropna()
    .tolist()
)

benign_urls = (
    benign_df["url"]
    .dropna()
    .tolist()
)


print("External phishing URLs:", len(phishing_urls))
print("External benign URLs:", len(benign_urls))


# =========================
# COMBINE DATA
# =========================

urls = phishing_urls + benign_urls

actual_labels = (
    [1] * len(phishing_urls)
    +
    [0] * len(benign_urls)
)


# =========================
# EXTRACT FEATURES
# =========================

features = []

for url in urls:

    features.append(
        extract_features(url)
    )


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


# Convert to DataFrame
X = pd.DataFrame(
    features,
    columns=feature_names
)


# =========================
# PREDICTION
# =========================

predictions = model.predict(X)


# =========================
# RESULTS
# =========================

accuracy = accuracy_score(
    actual_labels,
    predictions
)


print("\n========== EXTERNAL VALIDATION ==========")

print(
    "Total URLs:",
    len(urls)
)

print(
    "Accuracy:",
    round(accuracy * 100, 2),
    "%"
)


print("\nClassification Report:")

print(
    classification_report(
        actual_labels,
        predictions,
        target_names=[
            "Benign",
            "Phishing"
        ]
    )
)


print("Confusion Matrix:")

print(
    confusion_matrix(
        actual_labels,
        predictions
    )
)

# Save predictions
results = pd.DataFrame({
    "url": urls,
    "actual_label": actual_labels,
    "predicted_label": predictions
})

results.to_csv(
    "data/external_validation_results.csv",
    index=False
)

print("\nResults saved to:")
print("data/external_validation_results.csv")