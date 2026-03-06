from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import Optional, List
import os
from dotenv import load_dotenv

from app.services.mood_service import mood_service, MOOD_CATEGORIES
from app.services.song_library import get_songs_by_vibe, generate_yt_link
from app.services.playlist_service import generate_playlist_name
from app.core.database import session_scope, engine, Base
from app.models.mood_history import MoodHistory

# Flexible Environment Loading: Checks current and parent directories for .env
env_paths = [".env", "../.env"]
env_found = False
for path in env_paths:
    if os.path.exists(path):
        load_dotenv(dotenv_path=path)
        print(f"INFO: Loaded environment from {path}")
        env_found = True
        break

if not env_found:
    print("WARNING: No .env found. Ensure environment variables are set manually.")

# Initialize Database
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Slopahh Muzik API", version="1.0.0")

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic Schemas
class MoodInfo(BaseModel):
    label: str
    color_hex: str

class Recommendation(BaseModel):
    title: str
    artist: str
    album: str
    spotify_url: str
    youtube_url: str
    vibe_snippet: str

class RecommendResponse(BaseModel):
    mood: MoodInfo
    playlist_name: str
    recommendations: List[Recommendation]

class RecommendRequest(BaseModel):
    text_input: Optional[str] = ""
    mood_id: Optional[str] = None

@app.get("/api/v1/moods")
async def get_moods():
    moods = [
        { "id": "late_night", "label": "Late Night 🌙", "default_color": "#1A1A2E" },
        { "id": "gym", "label": "Power Hour 🔥", "default_color": "#E63946" },
        { "id": "focus", "label": "Deep Focus 🧠", "default_color": "#2A9D8F" },
        { "id": "nostalgic", "label": "Nostalgic 📼", "default_color": "#8D6E63" },
        { "id": "chill", "label": "Chill Vibe 🌊", "default_color": "#457B9D" }
    ]
    return moods

@app.post("/api/v1/recommend", response_model=RecommendResponse)
async def recommend(req: RecommendRequest):
    if not req.text_input and not req.mood_id:
        raise HTTPException(status_code=422, detail="Please provide a mood description or a mood ID")

    # 1. Determine the vibe (AI Detection)
    if req.mood_id:
        detected_mood = MOOD_CATEGORIES.get(req.mood_id, MOOD_CATEGORIES["chill"])
    else:
        detected_mood = mood_service.detect_mood(req.text_input)

    # 2. Determine Mood Key for lookups
    mood_key = next((k for k, v in MOOD_CATEGORIES.items() if v['label'] == detected_mood['label']), "chill")

    # 3. Generate a creative name
    playlist_name = generate_playlist_name(mood_key)

    # 4. Fetch Recommendations
    selected_songs = get_songs_by_vibe(mood_key, count=3)
    
    final_recommendations = []
    for song in selected_songs:
        final_recommendations.append({
            "title": song["title"],
            "artist": song["artist"],
            "album": song["album"],
            "spotify_url": song["spotify_url"],
            "youtube_url": generate_yt_link(song["title"], song["artist"]),
            "vibe_snippet": f"A quintessential {detected_mood['label']} track from '{song['album']}'."
        })

    # 5. Save to Mood History
    try:
        with session_scope() as session:
            history_entry = MoodHistory(
                user_input=req.text_input or req.mood_id,
                detected_mood=detected_mood['label'],
                playlist_name=playlist_name
            )
            session.add(history_entry)
    except Exception as e:
        print(f"Error saving history: {e}")

    return {
        "mood": {
            "label": detected_mood['label'],
            "color_hex": detected_mood['color_hex']
        },
        "playlist_name": playlist_name,
        "recommendations": final_recommendations
    }

@app.get("/api/v1/history")
async def get_history():
    try:
        with session_scope() as session:
            history = session.query(MoodHistory).order_by(MoodHistory.timestamp.desc()).limit(10).all()
            return [item.to_dict() for item in history]
    except Exception as e:
        print(f"Error fetching history: {e}")
        raise HTTPException(status_code=500, detail="Could not fetch history")

@app.get("/health_check")
async def health():
    return {"status": "ok", "framework": "fastapi"}

# Static Files - Serve Vite build if needed
if os.path.exists("static"):
    app.mount("/", StaticFiles(directory="static", html=True), name="static")

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("app.main:app", host="0.0.0.0", port=port, reload=True)
