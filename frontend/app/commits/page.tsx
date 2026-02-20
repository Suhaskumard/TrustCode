import Link from "next/link";
import { getJson } from "@/lib/api";

type Commit = {
  id: string;
  author: string;
  message: string;
  risk_score: number;
  risk_level: string;
  failure_probability: number;
};

export default async function CommitsPage() {
  const commits = await getJson<Commit[]>("/api/commits");

  return (
    <section>
      <h2 className="mb-4 text-3xl font-bold">Commit Risk Table</h2>
      <div className="card overflow-x-auto">
        <table className="w-full text-left text-sm">
          <thead className="text-slate-400">
            <tr>
              <th>ID</th><th>Author</th><th>Message</th><th>Risk</th><th>Failure Prob.</th><th></th>
            </tr>
          </thead>
          <tbody>
            {commits.map((c) => (
              <tr key={c.id} className="border-t border-slate-800">
                <td className="py-3">{c.id}</td>
                <td>{c.author}</td>
                <td>{c.message}</td>
                <td>{c.risk_score} ({c.risk_level})</td>
                <td>{Math.round(c.failure_probability * 100)}%</td>
                <td><Link className="text-cyan-300" href={`/commit/${c.id}`}>Deep Dive</Link></td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </section>
  );
}
