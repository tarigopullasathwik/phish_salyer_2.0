def detect_social_engineering(text):
    """Detects psychological manipulation patterns: Urgency, Fear, Greed."""
    alerts = []
    score = 0

    if not text:
        return alerts, score

    text_lower = text.lower()

    # Fear/Urgency markers
    fear_urgency = ["limited", "act now", "suspended", "account", "blocked", "don't miss", "immediate"]
    count_fear = sum(1 for kw in fear_urgency if kw in text_lower)
    if count_fear >= 2:
        alerts.append(("Critical", "⚠️ Psychological Manipulation: Phishers create a sense of urgency or fear."))
        score += 30

    # Greed/Promise of unrealistic wealth
    greed_markers = ["guaranteed job", "high salary", "no interview", "win big", "rich quickly", "monthly 100000", "easy job"]
    count_greed = sum(1 for kw in greed_markers if kw in text_lower)
    if count_greed >= 2:
        alerts.append(("Warning", "🧠 Greed Vector: Unrealistic salary promises or 'guaranteed' job offers often hide scams."))
        score += 25

    # Direct Monetary Requests
    monetary_markers = ["registration fee", "pay now", "crypto payment", "security deposit", "bank transfer", "upfront"]
    count_money = sum(1 for kw in monetary_markers if kw in text_lower)
    if count_money >= 1:
        alerts.append(("Critical", "🚨 Financial Demand: Official job centers DO NOT ask for upfront 'registration' or 'security' fees."))
        score += 40

    return alerts, score
