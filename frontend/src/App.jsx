import { useState, useEffect, useRef } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import { Sparkles, Search, Shuffle, Headphones, Youtube, Globe } from 'lucide-react'
import { apiService } from './services/api'
import { VibeResults } from './components/VibeResults'
import { InteractiveVisualizer } from './components/InteractiveVisualizer'
import './index.css'

function App() {
  const [inputText, setInputText] = useState('')
  const [moods, setMoods] = useState([])
  const [results, setResults] = useState(null)
  const [loading, setLoading] = useState(false)
  const [activeMood, setActiveMood] = useState(null)
  const [mousePos, setMousePos] = useState({ x: 0, y: 0 })
  const meshRef = useRef(null)

  useEffect(() => {
    const handleMouseMove = (e) => {
      setMousePos({ x: e.clientX, y: e.clientY });
    };
    window.addEventListener('mousemove', handleMouseMove);
    return () => window.removeEventListener('mousemove', handleMouseMove);
  }, []);

  useEffect(() => {
    apiService.getMoods()
      .then(data => setMoods(data))
      .catch(err => console.error("Error fetching moods:", err))
  }, [])

  // Dynamic Reactive Background Mesh logic
  useEffect(() => {
    if (results?.mood?.color_hex) {
      document.documentElement.style.setProperty('--accent-primary', results.mood.color_hex);
      // Generate a complementary/offset color for the second gradient point
      const secondaryColor = results.mood.color_hex + '88'; // add transparency or shift
      document.documentElement.style.setProperty('--accent-secondary', '#7000ff');
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
      console.error(err);
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
      <div className="vibe-mesh" ref={meshRef}></div>
      <div
        className="cursor-glow"
        style={{
          left: `${mousePos.x}px`,
          top: `${mousePos.y}px`
        }}
      ></div>
      <InteractiveVisualizer />

      <header>
        <motion.div
          initial={{ opacity: 0, y: -20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8, ease: "easeOut" }}
        >
          <p className="subtitle" style={{ marginBottom: '0.5rem', letterSpacing: '2px', fontWeight: 800 }}>
            <Sparkles size={14} style={{ display: 'inline', marginRight: '5px' }} /> AI-CURATED SOUNDSCAPES
          </p>
          <h1>Slopahh <br /><span className="highlight-text">Mood Muzik</span></h1>
          <p className="subtitle">
            Transcend your current state through generative audio matching. Describe your vibe or select a portal.
          </p>
        </motion.div>
      </header>

      <main>
        <motion.div
          className="input-portal"
          initial={{ opacity: 0, scale: 0.95 }}
          animate={{ opacity: 1, scale: 1 }}
          transition={{ delay: 0.2, duration: 0.8 }}
        >
          <div style={{ position: 'absolute', right: '30px', top: '50%', transform: 'translateY(-50%)', color: 'var(--text-dim)' }}>
            <Search size={24} />
          </div>
          <input
            type="text"
            className="main-input"
            placeholder="How does your soul feel right now?"
            value={inputText}
            onChange={(e) => setInputText(e.target.value)}
            onKeyDown={(e) => e.key === 'Enter' && handleRecommendation()}
          />
        </motion.div>

        <motion.div
          className="mood-strip"
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 0.4 }}
        >
          {moods.map((m, i) => (
            <motion.button
              key={m.id}
              className={`mood-chip ${activeMood === m.id ? 'active' : ''}`}
              whileHover={{ scale: 1.05 }}
              whileTap={{ scale: 0.95 }}
              onClick={() => handleRecommendation(m.id)}
            >
              {m.label.split(' ')[0]}
            </motion.button>
          ))}
          <button className="mood-chip" onClick={triggerRandom} style={{ borderStyle: 'dashed' }}>
            <Shuffle size={14} style={{ marginRight: '8px' }} /> RANDOM
          </button>
        </motion.div>

        <AnimatePresence mode="wait">
          {loading && (
            <motion.div
              key="loader"
              className="loading-pulse"
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              exit={{ opacity: 0 }}
            >
              Analyzing the Frequency...
            </motion.div>
          )}

          {results && (
            <motion.div
              key="results"
              initial={{ opacity: 0, y: 40 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.8, cubicBezier: [0.23, 1, 0.32, 1] }}
            >
              <VibeResults results={results} />
            </motion.div>
          )}
        </AnimatePresence>
      </main>

      <footer style={{ marginTop: '8rem', textAlign: 'center', opacity: 0.3, fontSize: '0.8rem' }}>
        &copy; 2025 SLOPAHH MUZIK CORE // BUILT FOR THE IMMERSIVE WEB
      </footer>
    </div>
  )
}

export default App
