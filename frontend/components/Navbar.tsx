import Link from "next/link";

const links = [
  ["/", "Home"],
  ["/dashboard", "Dashboard"],
  ["/commits", "Commits"],
  ["/ownership-lab", "Ownership"],
  ["/merge-control", "Merge Control"],
  ["/developer-profile", "Developer"],
  ["/manager", "Manager"],
  ["/failure-analytics", "Failures"],
  ["/trust-model", "Trust Model"],
  ["/ci-insights", "CI Insights"],
  ["/research-lab", "Research"],
  ["/admin", "Admin"],
];

export function Navbar() {
  return (
    <nav className="border-b border-slate-800 bg-panel px-6 py-4">
      <div className="mx-auto flex max-w-6xl items-center justify-between gap-4">
        <h1 className="text-lg font-semibold text-cyan-400">TrustCode Platform</h1>
        <div className="flex flex-wrap gap-4 text-sm">
          {links.map(([href, label]) => (
            <Link key={href} href={href} className="text-slate-300 hover:text-cyan-300">
              {label}
            </Link>
          ))}
        </div>
      </div>
    </nav>
  );
}
