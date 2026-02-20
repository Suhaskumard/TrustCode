import { getJson } from "@/lib/api";

type Commit = { id: string; author: string; message: string };

type BlastRadius = {
  commit_id: string;
  owner: string;
  modules_impacted: number;
  upstream_downstream_dependencies: string[];
  blast_radius_score: number;
};

export default async function OwnershipLabPage() {
  const commits = await getJson<Commit[]>("/api/commits");
  const target = commits[0]?.id || "cmt-101";
  const blast = await getJson<BlastRadius>(`/api/ownership/blast-radius/${target}`);

  return (
    <section className="space-y-4">
      <h2 className="text-3xl font-bold">Code Ownership & Blast Radius Lab</h2>
      <div className="card">
        <p>Commit: {blast.commit_id}</p>
        <p>Owner: {blast.owner}</p>
        <p>Modules impacted: {blast.modules_impacted}</p>
        <p>Blast radius score: {blast.blast_radius_score}</p>
        <p className="mt-2 text-sm text-slate-400">Dependencies: {blast.upstream_downstream_dependencies.join(" → ")}</p>
      </div>
    </section>
  );
}
