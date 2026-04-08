import re
from app.utils.helpers import validate_email_format, extract_domain

FREE_PROVIDERS = ['gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com', 'icloud.com']

def check_email_intelligence(email=None, content=None):
    alerts = []
    score = 0

    if not email and not content:
        return alerts, score

    if email:
        if not validate_email_format(email):
            alerts.append(("Warning", "Invalid email format"))
            score += 10
        
        domain = extract_domain(email)
        if domain in FREE_PROVIDERS:
            alerts.append(("Warning", "📧 Business communication from a free provider (gmail, etc.) is suspicious."))
            score += 15

        # Domain mismatch check (Heuristic: If email domain doesn't match common business patterns)
        # e.g., 'amazon' in content but domain is 'xyz.com'
        if content and 'amazon' in content.lower() and domain != 'amazon.com':
            alerts.append(("Critical", "⚠️ Possible Email Spoofing: Sender domain mismatch detected for 'Amazon'."))
            score += 40

        # Suspicious patterns in username (e.g. random strings)
        username = email.split('@')[0]
        if re.search(r'[0-9]{4,}', username) or len(set(username)) < 3:
            alerts.append(("Warning", "Suspiciously random character pattern in email username."))
            score += 10

    if content:
        # Emergency/Urgency detection
        urgency_keywords = ["urgent", "account", "suspended", "immediately", "bank details", "verify account"]
        matches = [kw for kw in urgency_keywords if kw in content.lower()]
        if len(matches) >= 2:
            alerts.append(("Warning", "⚡ Phishing urgency pattern detected in email body."))
            score += 20

    return alerts, score
