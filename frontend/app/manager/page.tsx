import { KpiCard } from "@/components/KpiCard";
import { getJson } from "@/lib/api";

type RoleResponse = {
  focus: string;
  widgets: string[];
};

type Summary = {
  trust_score: number;
  high_risk_commits: number;
  avg_ci_time_min: number;
  selective_testing_savings_min: number;
};

export default async function ManagerPage() {
  const manager = await getJson<RoleResponse>("/api/roles/manager");
  const summary = await getJson<Summary>("/api/dashboard/summary");

  return (
    <section className="space-y-4">
      <h2 className="text-3xl font-bold">Manager Risk & Productivity View</h2>
      <p className="text-slate-300">Focus: {manager.focus}</p>
      <div className="grid gap-4 md:grid-cols-4">
        <KpiCard title="Trust Score" value={`${summary.trust_score}/100`} />
        <KpiCard title="High-Risk Commits" value={`${summary.high_risk_commits}`} />
        <KpiCard title="Avg CI Time" value={`${summary.avg_ci_time_min} min`} />
        <KpiCard title="Time Saved" value={`${summary.selective_testing_savings_min} min`} />
      </div>
      <div className="card">
        <h3 className="font-semibold text-cyan-300">Manager Widgets</h3>
        <ul className="mt-2 list-disc pl-5 text-sm text-slate-300">
          {manager.widgets.map((w) => (
            <li key={w}>{w}</li>
          ))}
        </ul>
      </div>
    </section>
  );
}
