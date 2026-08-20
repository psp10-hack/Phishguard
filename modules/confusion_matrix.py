import pandas as pd
import matplotlib.pyplot as plt

from sklearn.metrics import confusion_matrix


# Load external validation results
df = pd.read_csv(
    "data/external_validation_results.csv"
)


# Actual and predicted labels
actual = df["actual_label"]
predicted = df["predicted_label"]


# Create confusion matrix
cm = confusion_matrix(
    actual,
    predicted
)


print("Confusion Matrix:")
print(cm)


# Create graph
plt.figure(figsize=(7, 6))

plt.imshow(cm)

plt.title("PhishGuard External Confusion Matrix")

plt.xlabel("Predicted Label")
plt.ylabel("Actual Label")

plt.xticks(
    [0, 1],
    ["Benign", "Phishing"]
)

plt.yticks(
    [0, 1],
    ["Benign", "Phishing"]
)


# Add values inside cells
for i in range(2):

    for j in range(2):

        plt.text(
            j,
            i,
            cm[i, j],
            ha="center",
            va="center"
        )


plt.tight_layout()


# Save graph
plt.savefig(
    "data/confusion_matrix.png",
    dpi=300
)


print("\nConfusion matrix graph saved!")
print("data/confusion_matrix.png")