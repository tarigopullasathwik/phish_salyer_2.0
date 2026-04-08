# PhishSlayer Pro – Combined Cybersecurity Command Center

A production-grade, full-stack cybersecurity platform integrating real-time network monitoring, behavioral phishing analysis, and infrastructure forensics.

## 🚀 Key Features
- **Real-time SOC Dashboard:** Live threat alerts and network metrics streamed via High-performance WebSockets.
- **Deep Intelligence Center:** Multi-vector forensic analysis combining behavioral NLP with WHOIS, SSL, and DNS intelligence.
- **Network Forensic Engine:** Integrated packet sniffer and threat simulator for real-time monitoring of malicious vectors.
- **Elite Dark-Theme UI:** Professional SOC-inspired interface with Glassmorphism and real-time data visualization.

## 🏗️ Technical Architecture
- **Backend:** FastAPI (Python 3.8+)
- **Frontend:** React + Vite + Tailwind CSS
- **Communication:** Bi-directional WebSockets + RESTful API
- **Forensics:** WHOIS data, SSL verification, Heuristic NLP, and Packet Analysis.

## 🛠️ Combined Setup Instructions

### 1. Backend Engine
```bash
cd backend
pip install -r requirements.txt
python -m uvicorn app.main:app --reload --port 8000
```
*Accessible at `http://127.0.0.1:8000`. OpenAPI docs at `/docs`.*

### 2. Frontend Dashboard
```bash
cd frontend
npm install
npm run dev
```
*Accessible at `http://localhost:5173`.*

---

## 🛡️ Usage
Navigate to the **Cyber Intelligence Center** in the sidebar to run a deep scan on any suspicious text, URL, or email address. The command center will provide a real-time risk index and a detailed infrastructure report.

**Securing Careers and Infrastructure, One Packet at a Time.**
