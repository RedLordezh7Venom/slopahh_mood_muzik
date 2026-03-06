# Project Structure: Mood-Based Music Recommender

A clean, modular organization for our full-stack application.

```text
slopahh_muzik/
├── backend/                # FastAPI Application
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py         # Entry point
│   │   ├── api/            # Route handlers (v1/endpoints)
│   │   ├── core/           # Config, Security, Constants
│   │   ├── services/       # AI Mood Detection & Rec Logic
│   │   ├── models/         # SQLAlchemy DB Models
│   │   └── schemas/        # Pydantic Data Models
│   ├── data/               # SQLite db file location (local)
│   ├── tests/              # Pytest suite
│   ├── requirements.txt
│   └── Dockerfile
│
├── frontend/               # React (Vite) Application
│   ├── src/
│   │   ├── assets/         # Images, global styles
│   │   ├── components/     # UI Parts (MoodCard, MusicPlayer)
│   │   ├── hooks/          # Custom vibe-switch hooks
│   │   ├── services/       # API calling logic
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── public/             # Static assets (favicons, manifest)
│   ├── package.json
│   └── Dockerfile
│
├── infra/                  # Shared infrastructure/deploy config
│   ├── docker-compose.yml  # Orchestrates both services
│   └── nginx/              # (Optional) Reverse proxy config
│
├── .env.example            # Template for environment variables
├── .gitignore
├── data_flow.md
└── README.md
```

## Component Breakdown

### 🛠️ Backend (`/backend`)
*   **services/**: This is where the magic happens. We'll have a `mood_service.py` for AI interfacing and a `recommender.py` for picking the best tracks.
*   **data/**: While the DB is SQLite, we keep this folder to ensure the `.db` file has a consistent home for Docker volume mounting.

### 🎨 Frontend (`/frontend`)
*   **components/**: We'll split the UI into "VibeSelector", "RecommendationList", and "ThemeWrapper".
*   **services/**: Centralizes `fetch` calls so the components stay clean and focused on UI logic.

### 🐳 Infrastructure (`/infra`)
*   **docker-compose.yml**: Allows us to spin up both the API and the Web app with a single command: `docker-compose up`.
*   **Environment**: We store API keys (like Gemini or Spotify) in `.env`, keeping secrets out of the code.
