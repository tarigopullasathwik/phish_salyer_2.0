from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, List, Dict, Any
import base64

from app.services.scam_detector import scan_text
from app.services.email_intelligence import check_email_intelligence
from app.services.social_engineering_detector import detect_social_engineering
from app.services.file_analyzer import analyze_file
from app.services.network_analyzer import analyze_network
from app.services.blacklist_engine import check_blacklist
from app.utils.helpers import normalize_score

router = APIRouter()

class AnalysisRequest(BaseModel):
    text: Optional[str] = ""
    url: Optional[str] = ""
    email: Optional[str] = ""
    file_content: Optional[str] = ""
    filename: Optional[str] = ""

class AnalysisResponse(BaseModel):
    scam_score: float
    risk_level: str
    alerts: List[List[str]]
    network_analysis: Dict[str, Any]
    analysis_meta: Dict[str, Any]

def perform_comprehensive_analysis(data: AnalysisRequest):
    """Core analysis logic shared across endpoints."""
    text = data.text
    url = data.url
    email = data.email
    file_b64 = data.file_content
    filename = data.filename

    all_alerts = [] # Format: ["Severity", "Message"]
    total_score = 0
    network_analysis = {}

    # 1. Text Behavioral & Keyword Check
    if text:
        text_alerts, text_score = scan_text(text)
        all_alerts.extend([["Warning", a] for a in text_alerts])
        total_score += text_score

        soc_eng_alerts, soc_eng_score = detect_social_engineering(text)
        # soc_eng_alerts is already List[List[str]] like [["Severity", "Message"]]
        all_alerts.extend(soc_eng_alerts)
        total_score += soc_eng_score

    # 2. Email Intelligence
    if email or text:
        email_intel_alerts, email_intel_score = check_email_intelligence(email=email, content=text)
        all_alerts.extend(email_intel_alerts)
        total_score += email_intel_score

    # 3. Network & Infrastructure analysis
    if url:
        nw_alerts, nw_score, nw_data = analyze_network(url)
        all_alerts.extend(nw_alerts)
        total_score += nw_score
        network_analysis = nw_data

    # 4. Blacklist Check (Domain & Email)
    domain = url.split('//')[-1].split('/')[0] if url else None
    bl_alerts, bl_score = check_blacklist(domain=domain, email=email)
    all_alerts.extend(bl_alerts)
    total_score += bl_score

    # 5. Advanced Forensic File Scanning (Base64)
    if file_b64:
        try:
            file_data = base64.b64decode(file_b64)
            f_alerts, f_score = analyze_file(file_data, filename)
            all_alerts.extend(f_alerts)
            total_score += f_score
        except Exception as e:
            all_alerts.append(["Critical", f"❌ Forensic Scanner failure: {str(e)}"])

    # Normalize final score
    final_score = normalize_score(total_score)
    risk_level = "Low"
    if final_score > 70: risk_level = "High"
    elif final_score > 30: risk_level = "Medium"

    return {
        "scam_score": final_score,
        "risk_level": risk_level,
        "alerts": all_alerts,
        "network_analysis": network_analysis,
        "analysis_meta": {
            "forensics_active": True,
            "vectors_analyzed": len(all_alerts)
        }
    }

@router.post("/", response_model=AnalysisResponse)
async def analyze(request: AnalysisRequest):
    try:
        result = perform_comprehensive_analysis(request)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
