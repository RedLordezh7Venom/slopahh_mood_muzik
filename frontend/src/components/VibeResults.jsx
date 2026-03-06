import { motion } from 'framer-motion'
import { Headphones, Youtube, ArrowUpRight, Play, ExternalLink } from 'lucide-react'

export const VibeResults = ({ results }) => {
    if (!results) return null;

    return (
        <div className="playlist-reveal">
            <div className="playlist-meta">
                <motion.p
                    className="playlist-tag"
                    initial={{ opacity: 0, x: -20 }}
                    animate={{ opacity: 1, x: 0 }}
                    transition={{ delay: 0.2 }}
                >
                    {results.mood.label} SPECTRUM DETECTED
                </motion.p>
                <motion.h2
                    className="playlist-title"
                    initial={{ opacity: 0, k: -20 }}
                    animate={{ opacity: 1, k: 0 }}
                    transition={{ delay: 0.3 }}
                >
                    {results.playlist_name}
                </motion.h2>
            </div>

            <div className="song-grid">
                {results.recommendations.map((song, idx) => (
                    <SongOrb key={idx} song={song} index={idx} />
                ))}
            </div>
        </div>
    );
};

const SongOrb = ({ song, index }) => {
    return (
        <motion.div
            className="song-orb"
            initial={{ opacity: 0, y: 30 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{
                delay: 0.4 + (index * 0.1),
                duration: 0.8,
                ease: [0.23, 1, 0.32, 1]
            }}
            whileHover={{ scale: 1.02 }}
        >
            <div className="orb-glow"></div>

            <div className="song-orb-card">
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: '1.5rem' }}>
                    <div className="card-badge">{song.artist.split(' ')[0]}</div>
                    <motion.div whileHover={{ rotate: 45 }}>
                        <ArrowUpRight size={20} opacity={0.3} />
                    </motion.div>
                </div>

                <span className="song-label">{song.title}</span>
                <span className="song-sublabel">{song.artist} • {song.album}</span>

                {song.vibe_snippet && (
                    <p style={{ fontSize: '0.85rem', color: 'rgba(255,255,255,0.5)', marginBottom: '2rem', lineHeight: '1.6' }}>
                        {song.vibe_snippet}
                    </p>
                )}

                <div className="song-footer">
                    <motion.a
                        href={song.spotify_url}
                        target="_blank"
                        rel="noreferrer"
                        className="stream-btn"
                        whileHover={{ scale: 1.05 }}
                        whileTap={{ scale: 0.95 }}
                    >
                        <Play size={12} fill="currentColor" style={{ marginRight: '8px', display: 'inline' }} /> LISTEN
                    </motion.a>

                    <a href={song.youtube_url} target="_blank" rel="noreferrer" className="secondary-btn">
                        YOUTUBE <ExternalLink size={10} style={{ display: 'inline', marginLeft: '5px' }} />
                    </a>
                </div>
            </div>
        </motion.div>
    )
}
