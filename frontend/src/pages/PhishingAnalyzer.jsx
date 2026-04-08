import { useState } from "react";
import { api } from "../services/api";
import { Search, Loader2, AlertTriangle, CheckCircle, Globe, Mail, Shield, AlertCircle, FileSearch, Fingerprint } from "lucide-react";
import { Badge } from "../components/ui/Badge";

export default function PhishingAnalyzer() {
  const [formData, setFormData] = useState({
    text: "",
    url: "",
    email: ""
  });
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  const handleAnalyze = async () => {
    if (!formData.text && !formData.url && !formData.email) return;
    setLoading(true);
    setResult(null);
    try {
      const data = await api.advancedAnalyze(formData);
      setResult(data);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="space-y-6 max-w-5xl mx-auto pb-12">
      <div className="flex justify-between items-end">
        <div>
          <h1 className="text-3xl font-bold mb-2 flex items-center gap-3">
            <Shield className="w-8 h-8 text-indigo-400" />
            Cyber Intelligence Center
          </h1>
          <p className="text-slate-400">Integrated multi-vector forensic analysis combining behavioral heuristics, infrastructure intel, and scam signatures.</p>
        </div>
        <Badge variant="outline" className="border-indigo-500/30 text-indigo-400 px-3 py-1">
          <Fingerprint className="w-3 h-3 mr-2" />
          V2.0 FORENSICS ACTIVE
        </Badge>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Input Controls */}
        <div className="lg:col-span-2 space-y-6">
          <div className="glass-panel p-6 space-y-4">
            <h2 className="text-sm font-semibold uppercase tracking-wider text-slate-500 mb-2">Analysis Vectors</h2>
            
            <div className="space-y-4">
              <div>
                <label className="text-xs font-medium text-slate-400 mb-1.5 block flex items-center gap-2">
                  <Mail className="w-3 h-3" /> Email or Scam Content
                </label>
                <textarea
                  className="w-full bg-black/40 border border-white/10 rounded-lg p-3 text-sm focus:outline-none focus:ring-2 focus:ring-indigo-500/50 min-h-[120px] resize-none transition-all"
                  placeholder="Paste suspicious messages, job offers, or email bodies here..."
                  value={formData.text}
                  onChange={(e) => setFormData({...formData, text: e.target.value})}
                />
              </div>

              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div>
                  <label className="text-xs font-medium text-slate-400 mb-1.5 block flex items-center gap-2">
                    <Globe className="w-3 h-3" /> Suspicious URL
                  </label>
                  <input
                    type="text"
                    className="w-full bg-black/40 border border-white/10 rounded-lg p-2.5 text-sm focus:outline-none focus:ring-2 focus:ring-indigo-500/50 transition-all"
                    placeholder="e.g., https://verify-secure-login.com"
                    value={formData.url}
                    onChange={(e) => setFormData({...formData, url: e.target.value})}
                  />
                </div>
                <div>
                  <label className="text-xs font-medium text-slate-400 mb-1.5 block flex items-center gap-2">
                    <Mail className="w-3 h-3" /> Sender Address
                  </label>
                  <input
                    type="text"
                    className="w-full bg-black/40 border border-white/10 rounded-lg p-2.5 text-sm focus:outline-none focus:ring-2 focus:ring-indigo-500/50 transition-all"
                    placeholder="e.g., support@secure-hr-dept.io"
                    value={formData.email}
                    onChange={(e) => setFormData({...formData, email: e.target.value})}
                  />
                </div>
              </div>
            </div>

            <button
              onClick={handleAnalyze}
              disabled={loading || (!formData.text && !formData.url && !formData.email)}
              className="w-full mt-4 bg-indigo-600 hover:bg-indigo-500 text-white py-3 rounded-lg text-sm font-semibold transition-all disabled:opacity-50 flex items-center justify-center gap-2 shadow-lg shadow-indigo-500/20 active:scale-[0.98]"
            >
              {loading ? <Loader2 className="w-4 h-4 animate-spin" /> : <Shield className="w-4 h-4" />}
              {loading ? "Engaging Multi-Vector Intelligence..." : "Run Deep Investigation"}
            </button>
          </div>

          {/* How it works merged */}
          <div className="glass-panel p-5">
             <h3 className="font-semibold text-sm mb-3 flex items-center gap-2">
               <FileSearch className="w-4 h-4 text-indigo-400" />
               Consolidated Methodology
             </h3>
             <ul className="text-xs text-slate-400 space-y-2 leading-relaxed">
               <li className="flex gap-2">
                 <span className="text-indigo-500">●</span> 
                 <span><strong>Behavioral NLP:</strong> Identifies social engineering patterns, false urgency, and suspicious financial requests.</span>
               </li>
               <li className="flex gap-2">
                 <span className="text-indigo-500">●</span> 
                 <span><strong>Infrastucture Intel:</strong> Performs WHOIS lookups, SSL validation, and DNS reputation checks.</span>
               </li>
               <li className="flex gap-2">
                 <span className="text-indigo-500">●</span> 
                 <span><strong>Identity Validation:</strong> Checks for free provider spoofing and suspicious sender patterns.</span>
               </li>
             </ul>
          </div>
        </div>

        {/* Results column */}
        <div className="space-y-6">
          {!result && !loading && (
            <div className="glass-panel p-8 text-center flex flex-col items-center justify-center h-full border-dashed border-white/10">
              <div className="w-16 h-16 bg-white/5 rounded-full flex items-center justify-center mb-4">
                <AlertCircle className="w-8 h-8 text-slate-600" />
              </div>
              <h3 className="text-slate-500 font-medium">Ready for Ingestion</h3>
              <p className="text-xs text-slate-600 mt-2">Input analysis vectors to begin the automated forensic scan.</p>
            </div>
          )}

          {loading && (
            <div className="glass-panel p-8 text-center flex flex-col items-center justify-center h-full">
              <Loader2 className="w-12 h-12 text-indigo-500 animate-spin mb-4" />
              <h3 className="text-white font-medium">Scanning Vectors</h3>
              <p className="text-xs text-slate-400 mt-2">Connecting to global intelligence feeds...</p>
            </div>
          )}

          {result && (
            <div className="space-y-6 animate-in fade-in slide-in-from-right-4 duration-500">
               {/* Risk Score Card */}
               <div className="glass-panel p-6 border-l-4 overflow-hidden" style={{ borderLeftColor: result.risk_level === 'High' ? '#f43f5e' : result.risk_level === 'Medium' ? '#f59e0b' : '#10b981' }}>
                  <div className="flex justify-between items-center mb-6">
                    <span className="text-xs font-bold uppercase tracking-widest text-slate-500">Intelligence Report</span>
                    <Badge variant={result.risk_level}>{result.risk_level.toUpperCase()}</Badge>
                  </div>
                  
                  <div className="flex flex-col items-center mb-8">
                    <div className="relative w-32 h-32 flex items-center justify-center">
                      <svg className="w-full h-full -rotate-90">
                        <circle cx="64" cy="64" r="58" fill="none" stroke="currentColor" strokeWidth="8" className="text-white/5" />
                        <circle cx="64" cy="64" r="58" fill="none" stroke="currentColor" strokeWidth="8" strokeDasharray="364.4" strokeDashoffset={364.4 - (364.4 * result.scam_score / 100)} className={result.risk_level === 'High' ? 'text-danger' : result.risk_level === 'Medium' ? 'text-warning' : 'text-success'} />
                      </svg>
                      <div className="absolute flex flex-col items-center">
                        <span className="text-3xl font-bold font-mono">{Math.round(result.scam_score)}</span>
                        <span className="text-[10px] uppercase text-slate-500 font-bold">Risk Index</span>
                      </div>
                    </div>
                  </div>

                  <div className="space-y-4">
                    <h4 className="text-xs font-bold text-slate-400 uppercase">Analysis Findings ({result.analysis_meta.vectors_analyzed})</h4>
                    <div className="space-y-2 max-h-[300px] overflow-y-auto pr-2 custom-scrollbar">
                      {result.alerts.map((alert, idx) => (
                        <div key={idx} className="p-3 bg-black/40 rounded border border-white/5 flex gap-3 items-start">
                          <AlertTriangle className={`w-4 h-4 shrink-0 mt-0.5 ${alert[0] === 'Critical' ? 'text-danger' : 'text-warning'}`} />
                          <div className="space-y-1">
                            <span className="text-[10px] font-bold uppercase block opacity-50">{alert[0]}</span>
                            <p className="text-xs text-slate-300 leading-normal">{alert[1]}</p>
                          </div>
                        </div>
                      ))}
                      {result.alerts.length === 0 && (
                        <div className="p-3 bg-black/40 rounded border border-white/5 flex gap-3 items-start">
                          <CheckCircle className="w-4 h-4 text-success shrink-0 mt-0.5" />
                          <p className="text-xs text-slate-300">No malicious indicators detected in the primary scan.</p>
                        </div>
                      )}
                    </div>
                  </div>
               </div>

               {/* Network Metadata Card */}
               {result.network_analysis && Object.keys(result.network_analysis).length > 0 && (
                 <div className="glass-panel p-5 bg-indigo-500/5 border-indigo-500/20">
                   <h4 className="text-xs font-bold text-indigo-400 uppercase mb-4 flex items-center gap-2">
                     <Globe className="w-3 h-3" /> Infrastructure Recon
                   </h4>
                   <div className="space-y-3">
                     {result.network_analysis.domain && (
                       <div className="flex justify-between text-[11px]">
                         <span className="text-slate-500">Target Domain</span>
                         <span className="text-white font-mono">{result.network_analysis.domain}</span>
                       </div>
                     )}
                     <div className="flex justify-between text-[11px]">
                        <span className="text-slate-500">SSL Certificate</span>
                        <span className={result.network_analysis.has_ssl ? 'text-success' : 'text-danger'}>
                          {result.network_analysis.has_ssl ? 'VALID' : 'MISSING/EXPIRED'}
                        </span>
                     </div>
                     {result.network_analysis.registrar && (
                       <div className="flex justify-between text-[11px]">
                         <span className="text-slate-500">Registrar</span>
                         <span className="text-white">{result.network_analysis.registrar}</span>
                       </div>
                     )}
                   </div>
                 </div>
               )}
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
