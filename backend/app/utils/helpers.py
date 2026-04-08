import re

def validate_email_format(email):
    """Simple regex check for email format."""
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

def extract_domain(email):
    """Extract domain from email."""
    if '@' in email:
        return email.split('@')[-1]
    return None

def normalize_score(score):
    """Cap score at 100."""
    return min(100, score)
