import { getJson } from "@/lib/api";

export default async function DeveloperProfilePage() {
  const profile = await getJson<any>("/api/roles/developer");

  return (
    <section className="space-y-4">
      <h2 className="text-3xl font-bold">Developer Reliability Profile</h2>
      <div className="card">
        <p className="text-slate-300">Focus: {profile.focus}</p>
        <ul className="mt-2 list-disc pl-5 text-sm text-slate-300">
          {profile.widgets.map((w: string) => <li key={w}>{w}</li>)}
        </ul>
      </div>
    </section>
  );
}
