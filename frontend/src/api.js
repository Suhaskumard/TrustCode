import axios from 'axios'

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'

const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
})

export const analyzeRepo = async (repoUrl) => {
  try {
    const response = await api.post(`/analyze-repo/${encodeURIComponent(repoUrl)}`, {})
    return response.data
  } catch (error) {
    throw new Error(error.response?.data?.detail || 'Analysis failed')
  }
}

export default api

