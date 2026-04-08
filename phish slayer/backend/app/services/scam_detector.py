import re

SCAM_KEYWORDS = [
    r'registration fee',
    r'pay now',
    r'urgent hiring',
    r'limited seats',
    r'guaranteed job',
    r'no upfront fee',
    r'send money',
    r'work from home'
]

def scan_text(text):
    """Scans text for scam keywords."""
    alerts = []
    score = 0
    if not text:
        return alerts, score

    text_lower = text.lower()
    for pattern in SCAM_KEYWORDS:
        if re.search(pattern, text_lower):
            alerts.append(f"Keyword: '{pattern}' detected")
            score += 20

    return alerts, score
