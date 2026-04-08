from app.utils.helpers import validate_email_format, extract_domain

FREE_EMAIL_DOMAINS = ['gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com', 'icloud.com', 'protonmail.com']

def check_email(email):
    """Analyzes sender email for suspicious features."""
    alerts = []
    score = 0

    if not email:
        return alerts, score

    if not validate_email_format(email):
        alerts.append("Invalid email format")
        score += 10
        return alerts, score

    domain = extract_domain(email)
    if domain in FREE_EMAIL_DOMAINS:
        alerts.append(f"Free email domain used: {domain}")
        score += 15
    
    # Generic suspicious username patterns
    # e.g., 'hr-manager123' might be less common than 'realhr@amazon.com'
    if len(email.split('@')[0]) > 20:
        alerts.append("Suspiciously long email username")
        score += 5

    return alerts, score
