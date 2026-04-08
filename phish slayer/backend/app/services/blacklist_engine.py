import json
import os

BLACKLIST_FILE = os.path.join(os.path.dirname(__file__), 'blacklist.json')

def load_blacklist():
    if not os.path.exists(BLACKLIST_FILE):
        return {"domains": [], "emails": []}
    with open(BLACKLIST_FILE, 'r') as f:
        return json.load(f)

def save_blacklist(data):
    with open(BLACKLIST_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def check_blacklist(domain=None, email=None):
    blacklist = load_blacklist()
    alerts = []
    score = 0

    if domain and domain.lower() in [d.lower() for d in blacklist['domains']]:
        alerts.append(("Critical", "🛑 Known scam domain detected in threat database!"))
        score += 35

    if email and email.lower() in [e.lower() for e in blacklist['emails']]:
        alerts.append(("Critical", "🛑 Known malicious sender detected in threat database!"))
        score += 35

    return alerts, score

def add_to_blacklist(domain=None, email=None):
    blacklist = load_blacklist()
    if domain and domain.lower() not in [d.lower() for d in blacklist['domains']]:
        blacklist['domains'].append(domain.lower())
    if email and email.lower() not in [e.lower() for e in blacklist['emails']]:
        blacklist['emails'].append(email.lower())
    save_blacklist(blacklist)
