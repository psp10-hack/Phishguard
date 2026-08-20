import joblib
import pandas as pd
import matplotlib.pyplot as plt


# Load model
model = joblib.load(
    "models/phishguard_model.pkl"
)


# Feature names
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


# Get importance
importance = model.feature_importances_


# Create DataFrame
df = pd.DataFrame({
    "Feature": features,
    "Importance": importance
})


# Sort
df = df.sort_values(
    "Importance",
    ascending=True
)


# Create graph
plt.figure(figsize=(10, 7))

plt.barh(
    df["Feature"],
    df["Importance"]
)

plt.xlabel("Importance")
plt.ylabel("Feature")
plt.title("PhishGuard Feature Importance")

plt.tight_layout()


# Save graph
plt.savefig(
    "data/feature_importance.png",
    dpi=300
)


print("Feature importance graph saved!")
print("data/feature_importance.png")