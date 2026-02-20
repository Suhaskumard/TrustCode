const API = process.env.NEXT_PUBLIC_API_BASE_URL || "http://localhost:8000";

export async function getJson<T>(path: string): Promise<T> {
  const res = await fetch(`${API}${path}`, { cache: "no-store" });
  if (!res.ok) {
    throw new Error(`Request failed: ${path}`);
  }
  return res.json();
}
