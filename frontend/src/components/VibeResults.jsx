/**
 * Component to render the generated playlist name with mood flair
 */
export const PlaylistHeader = ({ moodLabel, playlistName }) => {
    return (
        <div className="playlist-header">
            <p style={{
                textTransform: 'uppercase',
                fontSize: '0.7rem',
                color: 'var(--vibe-color)',
                marginBottom: '5px',
                fontWeight: 'bold'
            }}>
                {moodLabel} FOUND IN DATABASE
            </p>
            <h2 className="playlist-title">&gt; {playlistName}</h2>
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
                <div key={idx} className="song-card">
                    <div className="song-info">
                        <span className="song-title">{song.title}</span>
                        <br />
                        <span className="song-artist">{song.artist} // {song.album}</span>
                        <p style={{ fontSize: '0.7rem', marginTop: '5px', opacity: 0.8, fontStyle: 'italic' }}>
                            # {song.vibe_snippet || `A perfect track for your ${moodLabel} vibe.`}
                        </p>
                    </div>
                    <div className="song-actions">
                        {song.spotify_url && (
                            <a href={song.spotify_url} target="_blank" rel="noreferrer" className="action-btn" title="Spotify">
                                [SPOTIFY]
                            </a>
                        )}
                        {song.youtube_url && (
                            <a href={song.youtube_url} target="_blank" rel="noreferrer" className="action-btn" title="YouTube">
                                [YOUTUBE]
                            </a>
                        )}
                    </div>
                </div>
            ))}
        </div>
    );
};
