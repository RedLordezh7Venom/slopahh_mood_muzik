from app.core.database import engine, Base
from app.models.mood_history import MoodHistory

def init_db():
    print("Initializing the database...")
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully.")

if __name__ == "__main__":
    init_db()
