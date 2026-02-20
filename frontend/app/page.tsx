import Link from "next/link";

const featureCards = [
  "Predictive risk scoring before CI starts",
  "Trust-based merge gate with auto PR feedback",
  "Code ownership + blast radius intelligence",
  "Role dashboards for Developer, Manager, and Admin",
  "Research comparison metrics (before vs after Trust Loop)",
];

export default function HomePage() {
  return (
    <section className="space-y-8">
      <div className="space-y-4">
        <h2 className="text-4xl font-bold">Developer Trust & Code Reliability Platform</h2>
        <p className="max-w-3xl text-slate-300">
          Enterprise-style DevEx intelligence with explainable AI insights, CI cost optimization,
          and governance-friendly merge controls.
        </p>
      </div>

      <div className="grid gap-3 md:grid-cols-2">
        {featureCards.map((feature) => (
          <div key={feature} className="card text-sm text-slate-300">
            {feature}
          </div>
        ))}
      </div>

      <div className="flex gap-4">
        <Link className="rounded-lg bg-cyan-500 px-4 py-2 font-semibold text-slate-950" href="/dashboard">
          Open Dashboard
        </Link>
        <Link className="rounded-lg border border-slate-600 px-4 py-2" href="/research-lab">
          View Research Metrics
        </Link>
      </div>
    </section>
  );
}
