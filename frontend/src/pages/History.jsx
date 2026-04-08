import { useAlertStore } from "../store/useAlertStore";
import { Badge } from "../components/ui/Badge";
import { Clock, Download } from "lucide-react";

export default function History() {
  const alerts = useAlertStore(state => state.alerts);

  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center mb-2">
         <div>
          <h1 className="text-3xl font-bold mb-2 flex items-center gap-3">
            <Clock className="w-8 h-8 text-blue-400" />
            Alert History
          </h1>
          <p className="text-slate-400">Chronological log of all recorded security events.</p>
        </div>
        
        <button disabled className="bg-white/5 border border-white/10 px-4 py-2 rounded-lg text-sm text-slate-400 flex flex-items gap-2 cursor-not-allowed opacity-50">
           <Download className="w-4 h-4" />
           Export CSV
        </button>
      </div>

      <div className="glass-panel overflow-hidden">
         <div className="overflow-x-auto">
            <table className="w-full text-sm text-left">
               <thead className="text-xs text-slate-400 uppercase bg-black/40 border-b border-white/10">
                  <tr>
                     <th className="px-6 py-4 font-medium">Timestamp</th>
                     <th className="px-6 py-4 font-medium">Source IP</th>
                     <th className="px-6 py-4 font-medium">Type</th>
                     <th className="px-6 py-4 font-medium">Severity</th>
                     <th className="px-6 py-4 font-medium">Message</th>
                  </tr>
               </thead>
               <tbody>
                  {alerts.map((alert) => (
                     <tr key={alert.id} className="border-b border-white/5 hover:bg-white/5 transition-colors">
                        <td className="px-6 py-4 font-mono text-slate-500">{new Date(alert.timestamp).toLocaleString()}</td>
                        <td className="px-6 py-4 font-mono text-slate-300">{alert.ip}</td>
                        <td className="px-6 py-4 font-medium">{alert.type}</td>
                        <td className="px-6 py-4"><Badge variant={alert.severity}>{alert.severity.toUpperCase()}</Badge></td>
                        <td className="px-6 py-4 text-slate-400">{alert.message}</td>
                     </tr>
                  ))}
                  {alerts.length === 0 && (
                     <tr>
                        <td colSpan="5" className="px-6 py-12 text-center text-slate-500">No telemetry recorded yet.</td>
                     </tr>
                  )}
               </tbody>
            </table>
         </div>
      </div>
    </div>
  );
}
