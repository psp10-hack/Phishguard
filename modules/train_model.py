import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    roc_auc_score
)

# Load balanced dataset
df = pd.read_csv("data/balanced_dataset.csv")


# Features used by the model
features = [
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


# Input and output
X = df[features]
y = df["label"]


# Split into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# Create Random Forest model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)


# Train
model.fit(X_train, y_train)
joblib.dump(model, "models/phishguard_model.pkl")
print("\nModel saved successfully!")


# Predict
y_pred = model.predict(X_test)
y_probability = model.predict_proba(X_test)[:, 1]

# Results
print("Accuracy:", accuracy_score(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nROC-AUC Score:")
print(roc_auc_score(y_test, y_probability))

print("\nFeature Importance:")

importance = model.feature_importances_

for feature, value in sorted(
    zip(features, importance),
    key=lambda x: x[1],
    reverse=True
):
    print(f"{feature:15}: {value:.4f}")