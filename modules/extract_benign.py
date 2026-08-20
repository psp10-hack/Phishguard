import pandas as pd


# Input file
INPUT_FILE = "/Users/pramukhsprasad/Downloads/top-1m.csv"

# Output file
OUTPUT_FILE = "data/benign_10000.csv"


# Read CSV without assuming a header
df = pd.read_csv(
    INPUT_FILE,
    header=None,
    names=["rank", "domain"]
)


# Remove missing domains
df = df.dropna(subset=["domain"])


# Take first 10,000 domains
benign = df.head(10000).copy()


# Convert domains into URLs
benign["url"] = "https://" + benign["domain"].astype(str)


# Keep only URL column
benign = benign[["url"]]


# Save
benign.to_csv(
    OUTPUT_FILE,
    index=False
)


print("Done!")
print("Benign URLs extracted:", len(benign))
print("Saved to:", OUTPUT_FILE)

print("\nFirst 5 URLs:")
print(benign.head())
