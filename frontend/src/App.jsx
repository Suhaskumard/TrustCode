import { useState } from 'react'
import { analyzeRepo } from './api.js'

function App() {
  const [repoUrl, setRepoUrl] = useState('')
  const [loading, setLoading] = useState(false)
  const [analysis, setAnalysis] = useState(null)
  const [error, setError] = useState('')

  const handleAnalyze = async (e) => {
    e.preventDefault()
    if (!repoUrl) return
    
    setLoading(true)
    setError('')
    setAnalysis(null)
    
    try {
      const result = await analyzeRepo(repoUrl)
      setAnalysis(result)
    } catch (err) {
      setError(err.message)
    } finally {
      setLoading(false)
    }
  }

  const getTrustColor = (score) => {
    if (score >= 90) return 'trust-excellent'
    if (score >= 70) return 'trust-good'
    if (score >= 50) return 'trust-fair'
    return 'trust-poor'
  }

  return (
    <div className="min-h-screen py-12 px-4 sm:px-6 lg:px-8">
      <div className="max-w-4xl mx-auto">
        {/* Header */}
        <div className="text-center mb-12">
          <h1 className="text-5xl font-bold bg-gradient-to-r from-white to-gray-200 bg-clip-text text-transparent mb-4">
            TrustCode Platform
          </h1>
          <p className="text-xl text-gray-300 max-w-2xl mx-auto">
            AI-powered GitHub repository analysis with comprehensive trust scores
          </p>
        </div>

        {/* Input Form */}
        <form onSubmit={handleAnalyze} className="bg-white/10 backdrop-blur-xl rounded-3xl p-8 mb-12 border border-white/20 max-w-2xl mx-auto">
          <div className="flex flex-col sm:flex-row gap-4">
            <input
              type="url"
              value={repoUrl}
              onChange={(e) => setRepoUrl(e.target.value)}
              placeholder="https://github.com/username/repo"
              className="flex-1 px-6 py-4 bg-white/20 border border-white/30 rounded-2xl text-white placeholder-gray-400 focus:outline-none focus:ring-4 focus:ring-primary-500 focus:border-transparent transition-all duration-300"
              required
            />
            <button
              type="submit"
              disabled={loading}
              className="px-8 py-4 bg-gradient-to-r from-primary-600 to-primary-700 hover:from-primary-700 hover:to-primary-800 text-white font-semibold rounded-2xl shadow-2xl hover:shadow-primary/25 transform hover:-translate-y-1 transition-all duration-300 disabled:opacity-50 disabled:cursor-not-allowed whitespace-nowrap"
            >
              {loading ? 'Analyzing...' : 'Analyze Repo'}
            </button>
          </div>
        </form>

        {/* Error */}
        {error && (
          <div className="max-w-2xl mx-auto mb-8 p-6 bg-red-500/20 border border-red-500/50 rounded-2xl backdrop-blur-sm text-red-100 text-center animate-pulse">
            {error}
          </div>
        )}

        {/* Results */}
        {analysis && (
          <div className="grid lg:grid-cols-2 gap-8 max-w-6xl mx-auto">
            {/* Trust Score Card */}
            <div className="bg-white/10 backdrop-blur-xl rounded-3xl p-8 border border-white/20 col-span-full lg:col-span-1">
              <h3 className="text-2xl font-bold text-white mb-6 text-center">Trust Score</h3>
              <div className="relative">
                <div className={`radial-progress text-${getTrustColor(analysis.trust_score.overall)} text-5xl md:text-6xl font-black mx-auto mb-4 animate-pulse-slow`}
                     style={`--value: ${analysis.trust_score.overall}`} data-value={analysis.trust_score.overall}>
                  {analysis.trust_score.overall}
                </div>
                <p className={`text-4xl font-black text-center ${getTrustColor(analysis.trust_score.overall)} mb-2`}>
                  {analysis.trust_score.grade}
                </p>
                <p className="text-gray-300 text-center text-lg">Overall Trust</p>
              </div>
              
              {/* Factors */}
              <div className="grid grid-cols-2 gap-4 mt-8">
                {Object.entries(analysis.trust_score.factors).map(([key, value]) => (
                  <div key={key} className="text-center p-3 bg-white/5 rounded-xl">
                    <p className="text-2xl font-bold text-white">{value}</p>
                    <p className="text-sm text-gray-400 capitalize">{key}</p>
                  </div>
                ))}
              </div>
            </div>

            {/* Repo Info & Metrics */}
            <div className="space-y-6">
              <div className="bg-white/10 backdrop-blur-xl rounded-2xl p-6 border border-white/20">
                <h4 className="text-xl font-bold text-white mb-4">{analysis.repo_name}</h4>
                <a href={analysis.repo_url} target="_blank" rel="noreferrer" 
                   className="text-primary-400 hover:text-primary-300 text-sm underline flex items-center gap-2">
                  👁️ View on GitHub
                </a>
              </div>

              <div>
                <h4 className="text-xl font-bold text-white mb-4">Key Metrics</h4>
                <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
                  {analysis.metrics.map((metric, i) => (
                    <div key={i} className="bg-white/5 p-4 rounded-xl text-center">
                      <p className="text-2xl font-bold text-white">{metric.value.toLocaleString() || 0}</p>
                      <p className="text-sm text-gray-400">{metric.name}</p>
                    </div>
                  ))}
                </div>
              </div>
            </div>

            {/* AI Insights */}
            <div className="lg:col-span-2">
              <div className="bg-gradient-to-r from-green-500/10 to-blue-500/10 backdrop-blur-xl rounded-3xl p-8 border border-white/20">
                <h3 className="text-2xl font-bold text-white mb-6">🤖 AI Insights</h3>
                <div className="space-y-4 text-gray-200 leading-relaxed">
                  {Object.entries(analysis.ai_insights).map(([key, value]) => (
                    <div key={key}>
                      <p className="font-semibold text-primary-400 capitalize mb-1">{key}:</p>
                      <p>{value}</p>
                    </div>
                  ))}
                </div>
                <div className="mt-8 pt-6 border-t border-white/20">
                  <h4 className="text-lg font-bold text-white mb-4">📋 Summary</h4>
                  <p className="text-gray-200 italic">{analysis.summary}</p>
                </div>
                {analysis.recommendations.length > 0 && (
                  <div className="mt-6">
                    <h5 className="font-bold text-primary-300 mb-3">💡 Recommendations</h5>
                    <ul className="space-y-2">
                      {analysis.recommendations.map((rec, i) => (
                        <li key={i} className="flex items-start gap-2 text-gray-200">
                          <span className="text-primary-400 font-bold text-lg mt-0.5">→</span>
                          {rec}
                        </li>
                      ))}
                    </ul>
                  </div>
                )}
              </div>
            </div>
          </div>
        )}

        {/* Footer */}
        <div className="text-center mt-16 text-gray-400 text-sm">
          <p>Built with 🚀 by BLACKBOXAI | <a href="http://localhost:8000/docs" target="_blank" rel="noreferrer" className="underline hover:text-white">API Docs</a></p>
        </div>
      </div>
      
      <style jsx>{`
        .radial-progress {
          --border-width: 8px;
          --border-value: 80%;
          background: conic-gradient(var(--trust-excellent) calc(var(--value) * 1%), #374151 var(--value) * 1%);
          width: 200px;
          height: 200px;
          border-radius: 50%;
          position: relative;
          display: flex;
          align-items: center;
          justify-content: center;
        }
        .radial-progress::after {
          content: "";
          position: absolute;
          width: calc(100% - var(--border-width));
          height: calc(100% - var(--border-width));
          background: radial-gradient(circle at 30% 30%, #1f2937 0%, transparent 50%);
          border-radius: 50%;
        }
      `}</style>
    </div>
  )
}

export default App

