import socket
import whois
from datetime import datetime

def check_dns_intelligence(domain, ip):
    alerts = []
    score = 0

    # Domain Age Check (Already in url_checker, but let's consolidate or upgrade)
    try:
        w = whois.whois(domain)
        creation_date = w.creation_date
        if isinstance(creation_date, list):
            creation_date = creation_date[0]
        
        if creation_date:
            age_days = (datetime.now() - creation_date).days
            if age_days < 180: # Less than 6 months
                alerts.append(("Critical", f"🕒 Newly Registered Domain: (Age: {age_days} days). Phishers often create new domains for short-lived scams."))
                score += 25
    except Exception:
        # WHOIS check might fail for some domains
        alerts.append(("Info", "ℹ️ WHOIS Intelligence: Target domain data is private or unavailable (Possible 'stealth' registration)."))
        score += 10

    # IP Mismatch Patterns
    # If the domain has multiple IP addresses (sometimes used for high availability, sometimes for fast-flux phishing)
    try:
        host_info = socket.gethostbyname_ex(domain)
        ips = host_info[2]
        if len(ips) > 2:
            alerts.append(("Warning", f"🌐 Multiple IP addresses ({len(ips)}) detected for target. Possible fast-flux behavior?"))
            score += 15
    except socket.gaierror:
        pass

    # Blacklisted IP subnets (Simulated)
    # e.g., IPs starting with 192.168. (private) but appearing as public target
    if ip.startswith('192.168.') or ip.startswith('10.'):
        alerts.append(("Critical", "🛑 Internal IP Target: Domain resolves to a private network address (Possible spoof or internal threat)."))
        score += 30

    return alerts, score
