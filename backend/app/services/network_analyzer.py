import socket
import requests
import validators
from app.services.ssl_checker import check_ssl_extended
from app.services.dns_checker import check_dns_intelligence
from app.services.ip_intelligence import check_ip_intelligence

def analyze_network(url):
    """Coordinates DNS, SSL, and IP intelligence checks."""
    alerts = []
    score = 0
    network_data = {
        "ip": "Unknown",
        "location": "Unknown",
        "ssl_status": "Invalid",
        "domain_age": "Unknown",
        "threat_status": "Clean"
    }

    if not url:
        return alerts, score, network_data

    # Parse domain
    domain = url.split('//')[-1].split('/')[0] if '//' in url else url.split('/')[0]
    
    # DNS Check
    try:
        ip = socket.gethostbyname(domain)
        network_data["ip"] = ip
        dns_alerts, dns_score = check_dns_intelligence(domain, ip)
        alerts.extend(dns_alerts)
        score += dns_score
    except socket.gaierror:
        alerts.append(("Critical", "🌐 DNS Resolution Failed: Target domain could not be localized."))
        score += 30
        return alerts, score, network_data

    # SSL Check
    ssl_alerts, ssl_score, ssl_info = check_ssl_extended(domain)
    alerts.extend(ssl_alerts)
    score += ssl_score
    network_data["ssl_status"] = ssl_info.get("status", "Invalid")
    
    # IP Intelligence (Geo/ISP)
    ip_alerts, ip_score, ip_info = check_ip_intelligence(ip)
    alerts.extend(ip_alerts)
    score += ip_score
    network_data["location"] = f"{ip_info.get('country', 'Unknown')}, {ip_info.get('city', 'Unknown')}"

    # Threat Intelligence Hub (Simulated)
    # e.g., VirusTotal, Safe Browsing
    if domain.endswith('.xyz') or domain.endswith('.tk'):
        alerts.append(("Warning", "🚩 Flagged by Community Threat Intelligence source as 'Suspicious'."))
        score += 20
        network_data["threat_status"] = "Suspicious"

    return alerts, score, network_data
