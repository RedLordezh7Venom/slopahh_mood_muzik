# Slopahh Mood Muzik: Mood-Based Music Recommender 🎧

An AI-powered music recommendation system that translates your vibe into the perfect playlist.

## 🚀 Quick Start (Development)

### Prerequisites
- Python 3.10+
- Node.js & npm
- Docker (optional)

### Backend Setup
1. Navigate to `/backend`
2. Sync dependencies: `uv sync`
3. Run dev server: `uv run uvicorn app.main:app --reload`
4. **Production Run (Multiple Workers)**:
   - *On Linux (Standard)*:
     `uv run gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8000`
   - *On Windows (Alternative)*:
     `uv run uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4`

### Frontend Setup
1. Navigate to `/frontend`
2. Install dependencies: `npm install`
3. Run dev server: `npm run dev`

### Docker (Full Stack)
```bash
docker-compose -f infra/docker-compose.yml up --build
```

## 🛠️ Tech Stack
- **Backend**: FastAPI, SQLAlchemy, SQLite
- **AI**: Google Gemini API
- **Frontend**: React, Vite, Vanilla CSS
- **Deployment**: Docker

## 📄 Documentation
- [Implementation Plan](./implementation_plan.md)
- [Data Flow](./data_flow.md)
- [API Specs](./api_specs.md)
- [Folder Structure](./folder_structure.md)
