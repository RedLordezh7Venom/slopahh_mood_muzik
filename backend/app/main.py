from app import create_app
from app.services.mood_service import mood_service, MOOD_CATEGORIES
from app.services.song_library import get_songs_by_vibe, generate_yt_link
from app.services.playlist_service import generate_playlist_name
from app.core.database import session_scope
from app.models.mood_history import MoodHistory
import os

app = create_app()

def validate_song_payload(song_obj: dict):
    """
    Ensures that each recommendation object contains all required fields 
    as defined in the response schema.
    """
    required_fields = ["title", "artist", "album", "spotify_url", "youtube_url", "vibe_snippet"]
    for field in required_fields:
        if field not in song_obj or not song_obj[field]:
            return False
    return True

# Keeping routes here for initial development before moving to blueprints
from flask import request, jsonify

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/api/v1/moods', methods=['GET'])
def get_moods():
    moods = [
        { "id": "late_night", "label": "Late Night 🌙", "default_color": "#1A1A2E" },
        { "id": "gym", "label": "Power Hour 🔥", "default_color": "#E63946" },
        { "id": "focus", "label": "Deep Focus 🧠", "default_color": "#2A9D8F" },
        { "id": "nostalgic", "label": "Nostalgic 📼", "default_color": "#8D6E63" },
        { "id": "chill", "label": "Chill Vibe 🌊", "default_color": "#457B9D" }
    ]
    return jsonify(moods)

@app.route('/api/v1/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Missing request body"}), 400

    text_input = data.get('text_input', '')
    mood_id = data.get('mood_id')

    if not text_input and not mood_id:
        return jsonify({"error": "Please provide a mood description or a mood ID"}), 422

    # 1. Determine the vibe (AI Detection)
    if mood_id:
        detected_mood = MOOD_CATEGORIES.get(mood_id, MOOD_CATEGORIES["chill"])
    else:
        detected_mood = mood_service.detect_mood(text_input)

    # 2. Determine Mood Key for lookups
    mood_key = next((k for k, v in MOOD_CATEGORIES.items() if v['label'] == detected_mood['label']), "chill")

    # 3. Generate a creative name using Prefix + Suffix logic
    playlist_name = generate_playlist_name(mood_key)

    # 4. Fetch Recommendations using the dedicated retrieval function
    selected_songs = get_songs_by_vibe(mood_key, count=3)
    
    # Format and Validate for frontend response
    final_recommendations = []
    for song in selected_songs:
        song_entry = {
            "title": song["title"],
            "artist": song["artist"],
            "album": song["album"],
            "spotify_url": song["spotify_url"],
            "youtube_url": generate_yt_link(song["title"], song["artist"]),
            "vibe_snippet": f"A quintessential {detected_mood['label']} track from '{song['album']}'."
        }
        
        # Validation Step
        if validate_song_payload(song_entry):
            final_recommendations.append(song_entry)

    # 5. Save to Mood History (Robust Persistence)
    try:
        with session_scope() as session:
            history_entry = MoodHistory(
                user_input=text_input or mood_id,
                detected_mood=detected_mood['label'],
                playlist_name=playlist_name
            )
            session.add(history_entry)
            # Commit is handled by session_scope context manager
    except Exception as e:
        print(f"Error saving history: {e}")

    response = {
        "mood": {
            "label": detected_mood['label'],
            "color_hex": detected_mood['color_hex']
        },
        "playlist_name": playlist_name,
        "recommendations": final_recommendations
    }

    return jsonify(response)

@app.route('/api/v1/history', methods=['GET'])
def get_history():
    """Returns user mood history from the database."""
    try:
        with session_scope() as session:
            # Get the 10 most recent entries
            history = session.query(MoodHistory).order_by(MoodHistory.timestamp.desc()).limit(10).all()
            return jsonify([item.to_dict() for item in history])
    except Exception as e:
        print(f"Error fetching history: {e}")
        return jsonify({"error": "Could not fetch history"}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port, debug=True)
