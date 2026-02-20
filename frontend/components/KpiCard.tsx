type KpiCardProps = {
  title: string;
  value: string;
  hint?: string;
};

export function KpiCard({ title, value, hint }: KpiCardProps) {
  return (
    <div className="card">
      <p className="text-sm text-slate-400">{title}</p>
      <p className="mt-2 text-2xl font-bold text-cyan-300">{value}</p>
      {hint ? <p className="mt-1 text-xs text-slate-500">{hint}</p> : null}
    </div>
  );
}
