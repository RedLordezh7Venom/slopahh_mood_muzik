/**
 * Component to render the generated playlist name with mood flair
 */
export const PlaylistHeader = ({ moodLabel, playlistName }) => {
    return (
        <div className="playlist-header">
            <p className="subtitle">
                {moodLabel}
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
                <div key={idx} className="song-card">
                    <div className="song-info">
                        <div className="song-title">{song.title}</div>
                        <div style={{ fontSize: '12px', color: '#999', marginTop: '4px' }}>
                            Artist: {song.artist} <br />
                            Album: {song.album}
                        </div>
                        {song.vibe_snippet && (
                            <p style={{ fontSize: '11px', marginTop: '10px', color: '#666', fontStyle: 'italic' }}>
                                # {song.vibe_snippet}
                            </p>
                        )}
                    </div>
                    <div className="song-actions">
                        {song.youtube_url && (
                            <a href={song.youtube_url} target="_blank" rel="noreferrer" className="action-btn">
                                LISTEN ON YOUTUBE
                            </a>
                        )}
                        {song.spotify_url && (
                            <a href={song.spotify_url} target="_blank" rel="noreferrer" className="action-btn">
                                SPOTIFY
                            </a>
                        )}
                    </div>
                </div>
            ))}
        </div>
    );
};
