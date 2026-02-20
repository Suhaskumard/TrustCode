import { getJson } from "@/lib/api";

export default async function AdminPage() {
  const admin = await getJson<any>("/api/roles/admin");

  return (
    <section className="space-y-4">
      <h2 className="text-3xl font-bold">Admin / Professor Panel</h2>
      <div className="card">
        <p className="text-slate-300">Focus: {admin.focus}</p>
        <ul className="mt-2 list-disc pl-5 text-sm text-slate-300">
          {admin.widgets.map((w: string) => <li key={w}>{w}</li>)}
        </ul>
      </div>
    </section>
  );
}
