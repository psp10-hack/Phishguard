from urllib.parse import urlparse
import math
import re


def extract_features(url):

    parsed = urlparse(url)

    domain = parsed.netloc
    path = parsed.path
    query = parsed.query

    # Remove username/password if present
    domain = domain.split("@")[-1]

    # Remove port
    domain = domain.split(":")[0]

    # URL features
    url_len = len(url)
    dom_len = len(domain)

    # Check if domain is an IP address
    is_ip = 1 if re.match(r"^\d+\.\d+\.\d+\.\d+$", domain) else 0

    # TLD
    parts = domain.split(".")
    tld = parts[-1] if len(parts) > 1 else ""
    tld_len = len(tld)

    # Subdomains
    subdom_cnt = max(len(parts) - 2, 0)

    # Character counts
    letter_cnt = sum(c.isalpha() for c in url)
    digit_cnt = sum(c.isdigit() for c in url)

    special_cnt = sum(
        not c.isalnum() for c in url
    )

    eq_cnt = url.count("=")
    qm_cnt = url.count("?")
    amp_cnt = url.count("&")
    dot_cnt = url.count(".")
    dash_cnt = url.count("-")
    under_cnt = url.count("_")

    # Ratios
    letter_ratio = letter_cnt / url_len if url_len else 0
    digit_ratio = digit_cnt / url_len if url_len else 0
    spec_ratio = special_cnt / url_len if url_len else 0

    # HTTPS
    is_https = 1 if parsed.scheme.lower() == "https" else 0

    # Slashes
    slash_cnt = url.count("/")

    # Entropy
    frequency = {}

    for char in url:
        frequency[char] = frequency.get(char, 0) + 1

    entropy = 0

    for count in frequency.values():
        probability = count / url_len
        entropy -= probability * math.log2(probability)

    # Path and query
    path_len = len(path)
    query_len = len(query)

    return [
        url_len,
        dom_len,
        is_ip,
        tld_len,
        subdom_cnt,
        letter_cnt,
        digit_cnt,
        special_cnt,
        eq_cnt,
        qm_cnt,
        amp_cnt,
        dot_cnt,
        dash_cnt,
        under_cnt,
        letter_ratio,
        digit_ratio,
        spec_ratio,
        is_https,
        slash_cnt,
        entropy,
        path_len,
        query_len
    ]
def get_risk_factors(url, features):

    risk_factors = []

    # URL length
    if features[0] > 100:
        risk_factors.append("Very long URL")

    # Domain length
    if features[1] > 50:
        risk_factors.append("Long domain name")

    # IP address
    if features[2] == 1:
        risk_factors.append(
            "Uses an IP address instead of a domain"
        )

    # Subdomains
    if features[4] > 2:
        risk_factors.append(
            "Multiple subdomains"
        )

    # Digits
    if features[6] > 5:
        risk_factors.append(
            "High number of digits"
        )

    # Special characters
    if features[7] > 15:
        risk_factors.append(
            "High number of special characters"
        )

    # Letter ratio
    if features[14] < 0.5:
        risk_factors.append(
            "Low letter ratio"
        )

    # Digit ratio
    if features[15] > 0.2:
        risk_factors.append(
            "High digit ratio"
        )

    # Special-character ratio
    if features[16] > 0.3:
        risk_factors.append(
            "High special-character ratio"
        )

    # HTTPS
    if features[17] == 0:
        risk_factors.append(
            "Not using HTTPS"
        )

    # Entropy
    if features[19] > 4.5:
        risk_factors.append(
            "High URL entropy"
        )

    # Path
    if features[20] > 50:
        risk_factors.append(
            "Long URL path"
        )

    # Query
    if features[21] > 30:
        risk_factors.append(
            "Long query string"
        )


    # Suspicious keywords
    suspicious_keywords = [
        "login",
        "verify",
        "account",
        "password",
        "secure",
        "update",
        "confirm"
    ]

    url_lower = url.lower()

    found_keywords = []

    for word in suspicious_keywords:

        if word in url_lower:
            found_keywords.append(word)


    if found_keywords:

        risk_factors.append(
            "Suspicious keywords detected: "
            + ", ".join(found_keywords)
        )


    return risk_factors