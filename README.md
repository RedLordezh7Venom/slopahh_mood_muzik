# Slopahh Mood Muzik: Mood-Based Music Recommender 🎧

An AI-powered music recommendation system that translates your vibe into the perfect playlist.

## 🚀 Quick Start (Development)

### Prerequisites
- Python 3.10+
- Node.js & npm
- Docker (optional)

### Backend Setup
1. Navigate to `/backend`
2. Create a virtual environment: `python -m venv venv`
3. Install dependencies: `pip install -r requirements.txt`
4. Run server: `uvicorn app.main:app --reload`

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
