/**
 * Component to render the generated playlist name with mood flair
 */
export const PlaylistHeader = ({ moodLabel, playlistName }) => {
    return (
        <div className="playlist-header">
            <p style={{
                textTransform: 'uppercase',
                fontSize: '0.8rem',
                letterSpacing: '2px',
                color: 'var(--primary)',
                marginBottom: '0.5rem'
            }}>
                {moodLabel} Detected
            </p>
            <h2 className="playlist-title">{playlistName}</h2>
        </div>
    );
};

/**
 * Layout component for displaying a list of recommended songs
 */
export const RecommendationList = ({ songs, moodLabel }) => {
    if (!songs || songs.length === 0) return null;

    return (
        <div className="song-list">
            {songs.map((song, idx) => (
                <div key={idx} className="song-card" style={{ animationDelay: `${idx * 0.1}s` }}>
                    <div className="song-info">
                        <span className="song-title">{song.title}</span>
                        <span className="song-artist">{song.artist} • {song.album}</span>
                        <p style={{ fontSize: '0.8rem', marginTop: '0.5rem', opacity: 0.7 }}>
                            {song.vibe_snippet || `A perfect track for your ${moodLabel} vibe.`}
                        </p>
                    </div>
                    <div className="song-actions">
                        {song.spotify_url && (
                            <a href={song.spotify_url} target="_blank" rel="noreferrer" className="action-btn" title="Open in Spotify">
                                🟢
                            </a>
                        )}
                        {song.youtube_url && (
                            <a href={song.youtube_url} target="_blank" rel="noreferrer" className="action-btn" title="Search on YouTube">
                                🔴
                            </a>
                        )}
                    </div>
                </div>
            ))}
        </div>
    );
};
