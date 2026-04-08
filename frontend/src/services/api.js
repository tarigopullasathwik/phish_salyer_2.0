import axios from 'axios';

const API_BASE = 'http://localhost:8001/api';

export const api = {
  getStats: async () => {
    const res = await axios.get(`${API_BASE}/alerts/stats`);
    return res.data;
  },
  getAlerts: async () => {
     const res = await axios.get(`${API_BASE}/alerts`);
     return res.data;
  },
  analyzeContent: async (content) => {
    const res = await axios.post(`${API_BASE}/analyze`, { content });
    return res.data;
  },
  advancedAnalyze: async (payload) => {
    // payload: { text, url, email, file_content, filename }
    const res = await axios.post(`${API_BASE}/advanced-analyze/`, payload);
    return res.data;
  },
  simulateAttack: async () => {
    const res = await axios.post(`${API_BASE}/alerts/simulate`);
    return res.data;
  }
};
