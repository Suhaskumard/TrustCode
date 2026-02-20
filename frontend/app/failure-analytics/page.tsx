"use client";

import { useEffect, useState } from "react";
import {
  Bar,
  BarChart,
  CartesianGrid,
  ResponsiveContainer,
  Tooltip,
  XAxis,
  YAxis,
} from "recharts";

type Hotspot = {
  module: string;
  incidents: number;
};

type FailureTrends = {
  weekly_failure_rate: number[];
  hotspots: Hotspot[];
  current_avg_predicted_failure: number;
};

const API = process.env.NEXT_PUBLIC_API_BASE_URL || "http://localhost:8000";

export default function FailureAnalyticsPage() {
  const [data, setData] = useState<FailureTrends | null>(null);

  useEffect(() => {
    fetch(`${API}/api/analytics/failure-trends`)
      .then((res) => res.json())
      .then((result: FailureTrends) => setData(result));
  }, []);

  return (
    <section className="space-y-4">
      <h2 className="text-3xl font-bold">Failure Analytics & Root Cause</h2>
      <div className="card">
        <p className="text-slate-300">
          Current avg predicted failure: {Math.round((data?.current_avg_predicted_failure || 0) * 100)}%
        </p>
      </div>

      <div className="card h-80">
        <h3 className="mb-3 text-sm text-slate-400">Failure Hotspots by Module</h3>
        <ResponsiveContainer width="100%" height="100%">
          <BarChart data={data?.hotspots || []}>
            <CartesianGrid strokeDasharray="3 3" stroke="#334155" />
            <XAxis dataKey="module" stroke="#94a3b8" />
            <YAxis stroke="#94a3b8" />
            <Tooltip />
            <Bar dataKey="incidents" fill="#22d3ee" radius={[4, 4, 0, 0]} />
          </BarChart>
        </ResponsiveContainer>
      </div>
    </section>
  );
}
