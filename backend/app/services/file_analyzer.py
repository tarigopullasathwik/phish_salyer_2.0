import PyPDF2
import io
import re

def analyze_file(file_content, filename):
    alerts = []
    score = 0
    text = ""

    if not filename:
        return [] # No analysis if no filename

    # Basic text extraction for PDF / TXT
    if filename.endswith('.pdf'):
        try:
            reader = PyPDF2.PdfReader(io.BytesIO(file_content))
            for page in reader.pages:
                text += page.extract_text()
        except Exception:
            alerts.append(("Critical", "❌ Unable to parse PDF. Corrupt or encrypted file?"))
            return alerts, 20
    else: # Treat as text
        try:
            text = file_content.decode('utf-8')
        except UnicodeDecodeError:
            alerts.append(("Critical", "❌ Unsupported file format for scanning."))
            return alerts, 20

    if not text:
        return [], 0

    text_lower = text.lower()
    
    # Analyze extracted text
    scam_patterns = {
        "Payment Demand": [r'registration fee', r'security deposit', r'pay now', r'bank details', r'crypto'],
        "Unrealistic Promises": [r'guaranteed job', r'high salary', r'no interview', r'easy work'],
        "Fake Signatures/Verification": [r'verified by gov', r'stamped', r'authorized representative']
    }

    for category, patterns in scam_patterns.items():
        found = [p for p in patterns if re.search(p, text_lower)]
        if found:
            alerts.append(("Critical", f"🔍 File Analysis: {category} detected ('{found[0]}')."))
            score += 25

    # Look for generic formatting issues (e.g., poor grammar markers)
    suspicious_grammar = [r'congratulation you are', r'urgent inform', r'win prize']
    if any(re.search(p, text_lower) for p in suspicious_grammar):
         alerts.append(("Warning", "Low professional quality or grammar issues detected in document."))
         score += 15

    return alerts, score
