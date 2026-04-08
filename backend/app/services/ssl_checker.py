import ssl
import socket
from datetime import datetime
import OpenSSL

def check_ssl_extended(hostname):
    alerts = []
    score = 0
    ssl_info = {"status": "Invalid", "issuer": "Unknown", "expiry": "N/A"}

    # Basic timeout setup
    context = ssl.create_default_context()
    try:
        with socket.create_connection((hostname, 443), timeout=3) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()
                
                # Check Expiry
                not_after = datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y %Z')
                if not_after < datetime.now():
                    alerts.append(("Critical", f"🔐 Expired SSL Certificate: Target domain certificate expired on {not_after}."))
                    score += 25
                    ssl_info["status"] = "Expired"
                else:
                    ssl_info["status"] = "Valid"
                    ssl_info["expiry"] = cert['notAfter']

                # Issuer intelligence
                issuer = dict(x[0] for x in cert['issuer'])
                ssl_info["issuer"] = issuer.get('organizationName', 'Self-Signed / Private CA')
                if 'Let\'s Encrypt' in str(issuer):
                    # Not implicitly a scam, but VERY common in phishing
                    # alerts.append(("Info", "ℹ️ SSL Certificate issued by dynamic provider (Common for phishing)."))
                    pass
                elif 'organizationName' not in issuer:
                    alerts.append(("Warning", "🛡️ Untrusted Certificate Authority: Issuer does not provide public organization info."))
                    score += 15

    except ssl.SSLError:
        alerts.append(("Critical", "🔐 SSL Handshake Error: Target site does not support secure HTTPS or uses an invalid certificate."))
        score += 30
        ssl_info["status"] = "Invalid"
    except (socket.timeout, ConnectionRefusedError):
        alerts.append(("Critical", "🌐 Target site does not support secure HTTPS (No port 443 detected)."))
        score += 25
        ssl_info["status"] = "Missing"
    except Exception:
         ssl_info["status"] = "Unknown"

    return alerts, score, ssl_info
