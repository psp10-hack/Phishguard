def detect_suspicious_features(features):
    warnings = []

    if features["has_ip"]:
        warnings.append({
            "type": "ip_address",
            "message": "URL uses an IP address"
        })

    if not features["uses_https"]:
        warnings.append({
            "type": "no_https",
            "message": "URL does not use HTTPS"
        })

    if features["subdomain_count"] >= 2:
        warnings.append({
            "type": "multiple_subdomains",
            "message": "Multiple subdomains detected"
        })

    if features["length"] > 75:
        warnings.append({
            "type": "long_url",
            "message": "URL is unusually long"
        })

    if features["entropy"] > 4.5:
        warnings.append({
            "type": "high_entropy",
            "message": "URL contains highly varied characters"
        })

    for word in features["suspicious_keywords"]:
        warnings.append({
            "type": "suspicious_keyword",
            "message": "Suspicious keyword detected: " + word
        })

    return warnings