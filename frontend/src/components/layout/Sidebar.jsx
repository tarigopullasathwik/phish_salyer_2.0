import { NavLink } from 'react-router-dom';
import { Shield, LayoutDashboard, Activity, Search, Clock } from 'lucide-react';
import { clsx } from 'clsx';
import { twMerge } from "tailwind-merge";
import MatrixRainingCode from '../ui/MatrixRainingCode';

function cn(...inputs) {
  return twMerge(clsx(inputs));
}

export default function Sidebar() {
  const routes = [
    { name: 'Dashboard', path: '/dashboard', icon: LayoutDashboard },
    { name: 'Network Monitor', path: '/network', icon: Activity },
    { name: 'Phishing Analyzer', path: '/analyzer', icon: Search },
    { name: 'History', path: '/history', icon: Clock },
  ];

  return (
    <div className="w-64 border-r border-white/10 bg-black/40 backdrop-blur-xl h-screen sticky top-0 flex flex-col hidden lg:flex shrink-0 shadow-2xl z-20 relative overflow-hidden group">
      {/* Matrix background specifically inside the sidebar */}
      <MatrixRainingCode className="absolute inset-0 pointer-events-none -z-10 opacity-30 transition-opacity duration-1000 group-hover:opacity-50" />

      <div className="h-16 flex items-center gap-3 px-6 border-b border-white/10 relative z-10">
        <div className="p-1.5 bg-primary/20 text-primary rounded-lg shadow-[0_0_15px_rgba(16,185,129,0.3)]">
          <Shield className="w-6 h-6" />
        </div>
        <span className="font-bold text-lg tracking-wide text-transparent bg-clip-text bg-gradient-to-r from-primary to-emerald-400">
          PhishSlayer
        </span>
      </div>
      
      <div className="flex-1 py-6 px-4 space-y-1 relative z-10">
        {routes.map((route) => (
          <NavLink
            key={route.name}
            to={route.path}
            className={({ isActive }) => cn(
              "flex items-center gap-3 px-3 py-2.5 rounded-lg transition-all duration-200 group/link text-sm font-medium",
              isActive 
                ? "bg-primary/20 text-primary border border-primary/30 text-shadow-glow shadow-[0_0_15px_rgba(16,185,129,0.2)]" 
                : "text-slate-400 hover:bg-white/5 hover:text-slate-200"
            )}
          >
            {({ isActive }) => (
              <>
                <route.icon className={cn("w-5 h-5 transition-colors", isActive ? "text-primary filter drop-shadow-[0_0_5px_rgba(16,185,129,0.8)]" : "text-slate-500 group-hover/link:text-slate-300")} />
                {route.name}
              </>
            )}
          </NavLink>
        ))}
      </div>
      
      <div className="p-4 border-t border-white/10 relative z-10">
        <div className="px-3 py-3 rounded-lg bg-black/40 backdrop-blur-md border border-primary/20 flex items-center justify-between">
           <div className="flex items-center gap-2">
             <div className="w-2 h-2 rounded-full bg-success animate-pulse shadow-[0_0_8px_#10b981]" />
             <span className="text-xs text-primary font-mono opacity-80 z-20">SYS_ONLINE</span>
           </div>
        </div>
      </div>
    </div>
  );
}
