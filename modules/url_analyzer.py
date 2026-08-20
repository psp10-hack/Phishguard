from urllib.parse import urlparse
import ipaddress
import math


def calculate_entropy(text):
    characters = {}

    for char in text:
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1

    length = len(text)

    entropy = 0

    for char in characters:
        probability = characters[char] / length
        entropy -= probability * math.log2(probability)

    return entropy


def analyze_url(url):
    result = urlparse(url)

    if result.scheme not in ["http", "https"]:
        return None

    if result.hostname is None:
        return None

    length = len(url)
    entropy = calculate_entropy(url)
    uses_https = result.scheme == "https"

    try:
        ipaddress.ip_address(result.hostname)
        has_ip = True
    except ValueError:
        has_ip = False

    parts = result.hostname.split(".")
    subdomain_count = len(parts) - 2

    suspicious_keywords = [
        "login",
        "verify",
        "account",
        "password",
        "secure",
        "update",
        "confirm"
    ]

    found_keywords = []

    for word in suspicious_keywords:
        if word in url.lower():
            found_keywords.append(word)

    special_chars = "@-_?=%"
    special_count = 0

    for char in url:
        if char in special_chars:
            special_count += 1

    return {
        "length": length,
        "uses_https": uses_https,
        "has_ip": has_ip,
        "subdomain_count": subdomain_count,
        "suspicious_keywords": found_keywords,
        "special_char_count": special_count,
        "entropy": entropy
    }