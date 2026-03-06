from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.core.database import Base

class MoodHistory(Base):
    __tablename__ = "mood_history"

    id = Column(Integer, primary_key=True, index=True)
    user_input = Column(String)
    detected_mood = Column(String)
    playlist_name = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "user_input": self.user_input,
            "detected_mood": self.detected_mood,
            "playlist_name": self.playlist_name,
            "timestamp": self.timestamp.isoformat()
        }
