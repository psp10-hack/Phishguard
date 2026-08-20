from modules.url_analyzer import analyze_url
from modules.phishing_detector import detect_suspicious_features

url = input("Enter a URL: ")

features = analyze_url(url)

if features is None:
    print("Invalid URL")
else:
    warnings = detect_suspicious_features(features)

    print("Features:")
    print(features)

    print("\nWarnings:")

    if warnings:
        for warning in warnings:
            print("-", warning["message"])
    else:
        print("No suspicious features detected")