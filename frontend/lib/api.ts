const API_BASE = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'

export async function fetchTrending() {
  const res = await fetch(`${API_BASE}/api/trending`)
  if (!res.ok) throw new Error('Failed to fetch trending videos')
  return res.json()
}

export async function fetchRisingShorts() {
  const res = await fetch(`${API_BASE}/api/shorts/rising`)
  if (!res.ok) throw new Error('Failed to fetch rising shorts')
  return res.json()
}
