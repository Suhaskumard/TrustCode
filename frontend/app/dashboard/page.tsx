import { KpiCard } from "@/components/KpiCard";
import { getJson } from "@/lib/api";

export default async function DashboardPage() {
  const summary = await getJson<{
    trust_score: number;
    high_risk_commits: number;
    avg_ci_time_min: number;
    selective_testing_savings_min: number;
  }>("/api/dashboard/summary");

  return (
    <section className="space-y-4">
      <h2 className="text-3xl font-bold">System Overview Dashboard</h2>
      <div className="grid gap-4 md:grid-cols-4">
        <KpiCard title="Trust Score" value={`${summary.trust_score}/100`} hint="Team-wide reliability" />
        <KpiCard title="High-Risk Commits" value={`${summary.high_risk_commits}`} />
        <KpiCard title="Avg CI Time" value={`${summary.avg_ci_time_min} min`} />
        <KpiCard title="Selective Test Savings" value={`${summary.selective_testing_savings_min} min`} />
      </div>
    </section>
  );
}
