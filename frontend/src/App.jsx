import { useState, useEffect } from 'react'
import './index.css'
import { apiService } from './services/api'
import { PlaylistHeader, RecommendationList } from './components/VibeResults'

function App() {
  const [inputText, setInputText] = useState('')
  const [moods, setMoods] = useState([])
  const [results, setResults] = useState(null)
  const [loading, setLoading] = useState(false)
  const [activeMood, setActiveMood] = useState(null)

  // Fetch predefined moods on mount
  useEffect(() => {
    apiService.getMoods()
      .then(data => setMoods(data))
      .catch(err => console.error("Error fetching moods:", err))
  }, [])

  // Change background color based on mood
  useEffect(() => {
    if (results?.mood?.color_hex) {
      document.documentElement.style.setProperty('--vibe', results.mood.color_hex);
    } else {
      document.documentElement.style.setProperty('--vibe', '#00ff00');
    }
  }, [results])

  const handleRecommendation = async (id = null, text = null) => {
    setLoading(true)
    setResults(null)
    setActiveMood(id)

    try {
      const data = await apiService.getRecommendations({
        mood_id: id,
        text_input: text || inputText
      });
      setResults(data)
    } catch (err) {
      alert("Error: " + (err.message || "Failed to fetch vibe. Check server."));
    } finally {
      setLoading(false)
    }
  }

  const triggerRandom = () => {
    const randomMood = moods[Math.floor(Math.random() * moods.length)];
    handleRecommendation(randomMood.id);
  }

  return (
    <div className="container">
      <header>
        <h1>Slopahh Mood Muzik</h1>
        <p className="subtitle">Interactive Music Recommender</p>
      </header>

      <main>
        {/* Input Area */}
        <div className="vibe-input-group">
          <input
            type="text"
            className="main-input"
            placeholder="Search mood via text... (Enter to submit)"
            value={inputText}
            onChange={(e) => setInputText(e.target.value)}
            onKeyDown={(e) => e.key === 'Enter' && handleRecommendation()}
          />
        </div>

        {/* Categories */}
        <div className="mood-grid">
          {moods.map((m) => (
            <button
              key={m.id}
              className={`mood-btn ${activeMood === m.id ? 'active' : ''}`}
              onClick={() => handleRecommendation(m.id)}
            >
              {m.label}
            </button>
          ))}
        </div>

        <button className="random-btn" onClick={triggerRandom}>
          [ RANDOMIZE VIBE ]
        </button>

        {/* Status */}
        {loading && <div style={{ fontSize: '11px', color: 'var(--vibe)', textAlign: 'center' }}>DATA RETRIEVAL IN PROGRESS...</div>}

        {/* Results */}
        {results && (
          <div className="results-section">
            <PlaylistHeader
              moodLabel={results.mood.label}
              playlistName={results.playlist_name}
            />

            <RecommendationList
              songs={results.recommendations}
              moodLabel={results.mood.label}
            />
          </div>
        )}
      </main>
    </div>
  )
}

export default App
