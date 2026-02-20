import { getJson } from "@/lib/api";

type Commit = { id: string };

export default async function MergeControlPage() {
  const commits = await getJson<Commit[]>("/api/commits");
  const target = commits[0]?.id || "cmt-101";
  const policy = await getJson<{ block_threshold: number; review_threshold: number }>("/api/merge-gate/policy");
  const evaluation = await getJson<{ commit_id: string; risk_score: number; decision: string; auto_comment: string }>(
    `/api/merge-gate/evaluate/${target}`,
  );

  return (
    <section className="space-y-4">
      <h2 className="text-3xl font-bold">Trust-Based Merge Control Center</h2>
      <div className="grid gap-4 md:grid-cols-2">
        <div className="card">
          <h3 className="font-semibold text-cyan-300">Policy</h3>
          <p className="text-sm">Block threshold: {policy.block_threshold}</p>
          <p className="text-sm">Review threshold: {policy.review_threshold}</p>
        </div>
        <div className="card">
          <h3 className="font-semibold text-cyan-300">Latest Evaluation</h3>
          <p className="text-sm">Commit: {evaluation.commit_id}</p>
          <p className="text-sm">Risk score: {evaluation.risk_score}</p>
          <p className="text-sm">Decision: {evaluation.decision}</p>
          <p className="mt-2 text-xs text-slate-400">{evaluation.auto_comment}</p>
        </div>
      </div>
    </section>
  );
}
