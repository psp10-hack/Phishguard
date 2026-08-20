import pandas as pd
import os

# Find the main PhishGuard folder
BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

# Dataset location
INPUT_FILE = os.path.join(
    BASE_DIR,
    "data",
    "Dataset.csv"
)

# Output location
OUTPUT_FILE = os.path.join(
    BASE_DIR,
    "data",
    "balanced_dataset.csv"
)

# Load the dataset
df = pd.read_csv(INPUT_FILE)

# Show original class distribution
print("Original dataset:")
print(df["label"].value_counts())

# Separate benign and phishing URLs
benign = df[df["label"] == 0]
phishing = df[df["label"] == 1]

# Take 16,600 from each class
benign_sample = benign.sample(
    n=16600,
    random_state=42
)

phishing_sample = phishing.sample(
    n=16600,
    random_state=42
)

# Combine both classes
balanced = pd.concat(
    [benign_sample, phishing_sample],
    ignore_index=True
)

# Shuffle the dataset
balanced = balanced.sample(
    frac=1,
    random_state=42
).reset_index(drop=True)

# Save the balanced dataset
balanced.to_csv(
    OUTPUT_FILE,
    index=False
)

# Display results
print("\nBalanced dataset created!")
print("Total rows:", len(balanced))

print("\nClass distribution:")
print(balanced["label"].value_counts())

print("\nSaved to:")
print(OUTPUT_FILE)