import { getJson } from "@/lib/api";

type PageProps = { params: { id: string } };

export default async function CommitDeepDivePage({ params }: PageProps) {
  const data = await getJson<any>(`/api/commits/${params.id}`);

  return (
    <section className="space-y-4">
      <h2 className="text-3xl font-bold">Commit Deep Dive: {params.id}</h2>
      <div className="grid gap-4 md:grid-cols-2">
        <div className="card">
          <h3 className="font-semibold text-cyan-300">Explainable AI</h3>
          <ul className="mt-2 list-disc pl-5 text-sm text-slate-300">
            {data.risk.explanation.map((item: string) => <li key={item}>{item}</li>)}
          </ul>
        </div>
        <div className="card">
          <h3 className="font-semibold text-cyan-300">CI Recommendation</h3>
          <p className="mt-2 text-sm">Merge Gate: {data.ci.merge_gate}</p>
          <p className="text-sm">Test Scope: {data.ci.recommended_test_scope}</p>
          <p className="text-sm">Pipeline Estimate: {data.ci.estimated_pipeline_time_min} min</p>
        </div>
      </div>
    </section>
  );
}
