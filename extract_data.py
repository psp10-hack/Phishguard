import pandas as pd

# Tranco
df = pd.read_csv(
    "/Users/pramukhsprasad/Downloads/top-1m.csv",
    header=None,
    names=["rank", "domain"]
)

sample = df.sample(n=10000, random_state=42)

sample.to_csv("data/benign_10000.csv", index=False)

print("Done! Extracted 10,000 benign domains.")