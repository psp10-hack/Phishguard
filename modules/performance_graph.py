import matplotlib.pyplot as plt


# Performance values
tests = [
    "Internal Test",
    "External Test"
]

accuracy = [
    96.23,
    87.48
]


# Create graph
plt.figure(figsize=(8, 6))

plt.bar(
    tests,
    accuracy
)

plt.ylabel("Accuracy (%)")
plt.title("PhishGuard Model Performance")

plt.ylim(0, 100)


# Add values above bars
for i, value in enumerate(accuracy):

    plt.text(
        i,
        value + 1,
        f"{value:.2f}%",
        ha="center"
    )


plt.tight_layout()


# Save graph
plt.savefig(
    "data/performance_comparison.png",
    dpi=300
)


print("Performance graph saved!")
print("data/performance_comparison.png")