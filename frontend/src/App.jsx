import { useState, useEffect } from 'react'
import './index.css'

function App() {
  const [inputText, setInputText] = useState('')
  const [moods, setMoods] = useState([])
  const [results, setResults] = useState(null)
  const [loading, setLoading] = useState(false)
  const [activeMood, setActiveMood] = useState(null)

  // Fetch predefined moods on mount
  useEffect(() => {
    fetch('http://localhost:8000/api/v1/moods')
      .then(res => res.json())
      .then(data => setMoods(data))
      .catch(err => console.error("Error fetching moods:", err))
  }, [])

  // Change background color based on mood
  useEffect(() => {
    if (results?.mood?.color_hex) {
      document.body.style.backgroundColor = results.mood.color_hex;
    } else {
      document.body.style.backgroundColor = '#0f172a';
    }
  }, [results])

  const handleRecommendation = async (id = null, text = null) => {
    setLoading(true)
    setResults(null)
    setActiveMood(id)

    try {
      const response = await fetch('http://localhost:8000/api/v1/recommend', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          mood_id: id,
          text_input: text || inputText
        })
      })
      const data = await response.json()
      setResults(data)
    } catch (err) {
      console.error("Vibe error:", err)
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
        <p className="subtitle">AI-Powered Music for your current Vibe</p>
      </header>

      <main>
        {/* Text Input Section */}
        <div className="vibe-input-group">
          <input
            type="text"
            className="main-input"
            placeholder="Describe your vibe... (e.g., 'raining outside and I feel lonely')"
            value={inputText}
            onChange={(e) => setInputText(e.target.value)}
            onKeyDown={(e) => e.key === 'Enter' && handleRecommendation()}
          />
        </div>

        {/* Predefined Mood Buttons */}
        <div className="mood-grid">
          {moods.map((m) => (
            <button
              key={m.id}
              className={`mood-btn ${activeMood === m.id ? 'active' : ''}`}
              onClick={() => handleRecommendation(m.id)}
            >
              <span className="mood-icon">{m.label.split(' ')[1]}</span>
              <span>{m.label.split(' ')[0]}</span>
            </button>
          ))}
        </div>

        {/* Random Trigger */}
        <button className="random-btn" onClick={triggerRandom}>
          ✨ Surprise me with a random vibe
        </button>

        {/* Loading State */}
        {loading && <div style={{ textAlign: 'center', fontSize: '1.2rem' }}>Searching for the perfect tracks... 🎧</div>}

        {/* Results Container */}
        {results && (
          <div className="results-section">
            <div className="playlist-header">
              <p style={{ textTransform: 'uppercase', fontSize: '0.8rem', letterSpacing: '2px', color: 'var(--primary)' }}>
                {results.mood.label} Detected
              </p>
              <h2 className="playlist-title">{results.playlist_name}</h2>
            </div>

            <div className="song-list">
              {results.recommendations.map((song, idx) => (
                <div key={idx} className="song-card" style={{ animationDelay: `${idx * 0.1}s` }}>
                  <div className="song-info">
                    <span className="song-title">{song.title}</span>
                    <span className="song-artist">{song.artist} • {song.album}</span>
                    <p style={{ fontSize: '0.8rem', marginTop: '0.5rem', opacity: 0.7 }}>{song.vibe_snippet}</p>
                  </div>
                  <div className="song-actions">
                    <a href={song.spotify_url} target="_blank" rel="noreferrer" className="action-btn" title="Spotify">
                      🟢
                    </a>
                    <a href={song.youtube_url} target="_blank" rel="noreferrer" className="action-btn" title="YouTube">
                      🔴
                    </a>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}
      </main>
    </div>
  )
}

export default App
