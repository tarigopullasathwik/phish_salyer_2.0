BLACKLISTED_DOMAINS = [
    'fakecompany.com',
    'scamjobs.in',
    'amaz0n-jobs.com',
    'apple-refund.net',
    'paypa1.co.in'
]

def check_reputation(domain=None, email=None):
    """Local blacklist check."""
    alerts = []
    score = 0

    if not domain and not email:
        return alerts, score

    if domain and domain.lower() in [d.lower() for d in BLACKLISTED_DOMAINS]:
        alerts.append("Blacklisted domain detected (Direct match)")
        score += 30

    if email:
        email_domain = email.split('@')[-1]
        if email_domain.lower() in [d.lower() for d in BLACKLISTED_DOMAINS]:
            alerts.append(f"Email from blacklisted domain: {email_domain}")
            score += 30

    return alerts, score
