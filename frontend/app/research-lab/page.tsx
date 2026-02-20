import { KpiCard } from "@/components/KpiCard";
import { getJson } from "@/lib/api";

type ResearchData = {
  period: string;
  avg_risk_before: number;
  avg_risk_after: number;
  trust_gain_percent: number;
  deployment_failure_drop_percent: number;
};

export default async function ResearchLabPage() {
  const research = await getJson<ResearchData>("/api/research/comparison");

  return (
    <section className="space-y-4">
      <h2 className="text-3xl font-bold">Research Lab: Trust Loop Impact</h2>
      <p className="text-slate-300">Evaluation Period: {research.period}</p>
      <div className="grid gap-4 md:grid-cols-4">
        <KpiCard title="Avg Risk Before" value={`${research.avg_risk_before}`} />
        <KpiCard title="Avg Risk After" value={`${research.avg_risk_after}`} />
        <KpiCard title="Trust Gain" value={`${research.trust_gain_percent}%`} />
        <KpiCard title="Failure Drop" value={`${research.deployment_failure_drop_percent}%`} />
      </div>
    </section>
  );
}
