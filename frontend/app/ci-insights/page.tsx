import { KpiCard } from "@/components/KpiCard";
import { getJson } from "@/lib/api";

export default async function CIInsightsPage() {
  const ci = await getJson<any>("/api/ci/insights");

  return (
    <section className="space-y-4">
      <h2 className="text-3xl font-bold">CI Time & Cost Optimization</h2>
      <div className="grid gap-4 md:grid-cols-4">
        <KpiCard title="Avg Pipeline Time" value={`${ci.avg_pipeline_time_min} min`} />
        <KpiCard title="Monthly CI Cost" value={`$${ci.estimated_monthly_ci_cost_usd}`} />
        <KpiCard title="Time Saved" value={`${ci.selective_testing_time_saved_min} min`} />
        <KpiCard title="Flaky Test Rate" value={`${Math.round(ci.flaky_test_rate * 100)}%`} />
      </div>
    </section>
  );
}
