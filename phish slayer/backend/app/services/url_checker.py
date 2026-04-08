import requests
import validators
import whois
from datetime import datetime
import socket
import ssl

SUSPICIOUS_TLDS = ['.xyz', '.tk', '.ga', '.cf', '.ml', '.pw', '.bid', '.top']

def check_url(url):
    """Checks URL for SSL, domain age, and common phishing features."""
    alerts = []
    score = 0

    if not url:
        return alerts, score

    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url

    if not validators.url(url):
        alerts.append("Invalid URL format")
        score += 10
        return alerts, score

    domain = url.split('//')[-1].split('/')[0]

    # Check SSL
    try:
        response = requests.get(url, timeout=5)
        if not url.startswith('https://'):
            alerts.append("No SSL certificate (Site uses HTTP)")
            score += 20
    except requests.RequestException:
        alerts.append("Unreachable domain or invalid SSL")
        score += 15

    # Check TLD
    for tld in SUSPICIOUS_TLDS:
        if domain.endswith(tld):
            alerts.append(f"Suspicious TLD detected: {tld}")
            score += 15
            break

    # Check WHOIS for domain age (REAL CHECK)
    try:
        w = whois.whois(domain)
        creation_date = w.creation_date
        if isinstance(creation_date, list):
            creation_date = creation_date[0]
        
        if creation_date:
            age_days = (datetime.now() - creation_date).days
            if age_days < 180: # Less than 6 months
                alerts.append(f"Newly created domain (Age: {age_days} days)")
                score += 25
    except Exception:
        # WHOIS check might fail for some domains
        alerts.append("WHOIS data unavailable or privacy-protected")
        score += 10

    # URL Shorteners
    shorteners = ['bit.ly', 't.co', 'tinyurl.com', 'is.gd', 'buff.ly']
    if any(shortener in domain for shortener in shorteners):
        alerts.append("Shortened URL used (can hide destination)")
        score += 15

    return alerts, score
