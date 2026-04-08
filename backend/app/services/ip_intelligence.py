import requests

def check_ip_intelligence(ip):
    alerts = []
    score = 0
    ip_info = {"country": "Unknown", "city": "Unknown", "isp": "Unknown"}

    # Geo Intelligence (Free, low rate limit)
    try:
        response = requests.get(f"https://ipapi.co/{ip}/json/", timeout=5)
        if response.status_code == 200:
            data = response.json()
            ip_info["country"] = data.get("country_name", "Unknown")
            ip_info["city"] = data.get("city", "Unknown")
            ip_info["isp"] = data.get("org", "Unknown")
            
            # Risk Indicators based on Region (Simulated - some regions have higher fraud data)
            high_risk_countries = ["Nigeria", "Russia", "unknown"]
            if ip_info["country"] in high_risk_countries:
                alerts.append(("Warning", f"🌍 High-Risk Geo Location: Target server is located in {ip_info['country']}."))
                score += 20
            
            # Hosting provider intelligence
            scam_hosting_patterns = ["Namecheap", "Cloudflare", "DigitalOcean"] # Common legitimate hosting providers used for scams
            # Logic: If it's a known cheap or anonymous ISP, might add points?
            if any(p.lower() in ip_info["isp"].lower() for p in scam_hosting_patterns):
                 # Just informing
                 pass

    except (requests.RequestException, ValueError):
        pass # Handle API limit or unreachable services quietly

    # Port Intelligence (Basic check 80 / 443)
    # Already handled partly in ssl_checker

    return alerts, score, ip_info
