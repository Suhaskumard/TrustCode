import { getJson } from "@/lib/api";

export default async function TrustModelPage() {
  const model = await getJson<any>("/api/trust-model");

  return (
    <section className="space-y-4">
      <h2 className="text-3xl font-bold">Trust Model Explainability</h2>
      <div className="card">
        <p className="text-slate-300">{model.model}</p>
        <pre className="mt-3 overflow-x-auto text-xs text-cyan-300">{JSON.stringify(model.weights, null, 2)}</pre>
        <ul className="mt-3 list-disc pl-5 text-sm text-slate-300">
          {model.explainability.map((e: string) => <li key={e}>{e}</li>)}
        </ul>
      </div>
    </section>
  );
}
