import os
import json
import random
import google.generativeai as genai
from typing import Dict, Any

# Define high-fidelity mood categories for the system
MOOD_CATEGORIES = {
    "late_night": {
        "label": "Late Night 🌙",
        "color_hex": "#1A1A2E",
        "search_tags": ["lofi", "ambient", "night", "synthwave", "slowed"],
        "playlist_prefix": "3AM Thoughts",
        "keywords": ["night", "late", "dark", "moon", "midnight", "sleepy", "quiet", "stars"]
    },
    "gym": {
        "label": "Power Hour 🔥",
        "color_hex": "#E63946",
        "search_tags": ["phonk", "aggressive", "high-tempo", "metal", "hip-hop"],
        "playlist_prefix": "Main Character Energy",
        "keywords": ["gym", "workout", "pump", "training", "lift", "beast", "energy", "hard", "fast", "power"]
    },
    "focus": {
        "label": "Deep Focus 🧠",
        "color_hex": "#2A9D8F",
        "search_tags": ["classical", "minimalism", "drone", "study-beats"],
        "playlist_prefix": "Work Flow",
        "keywords": ["study", "work", "code", "coding", "focus", "concentration", "learn", "office", "productive"]
    },
    "nostalgic": {
        "label": "Nostalgic 📼",
        "color_hex": "#8D6E63",
        "search_tags": ["80s", "retro", "warm", "vinyl", "dream-pop"],
        "playlist_prefix": "Rewind",
        "keywords": ["memory", "old", "retro", "past", "childhood", "remember", "yesterday", "vibes", "back", "rain"]
    },
    "heartbreak": {
        "label": "Heartbreak 💔",
        "color_hex": "#4A4E69",
        "search_tags": ["sad", "acoustic", "ballad", "emo", "emotional"],
        "playlist_prefix": "Blue Hours",
        "keywords": ["sad", "broken", "pain", "crying", "tears", "lonely", "alone", "miss", "hurt", "depressed"]
    },
    "chill": {
        "label": "Chill Vibe 🌊",
        "color_hex": "#457B9D",
        "search_tags": ["indie", "surfer", "relaxed", "summer", "easy-listening"],
        "playlist_prefix": "Coastal Drift",
        "keywords": ["chill", "relax", "easy", "calm", "vibe", "beach", "summer", "peaceful", "soft"]
    }
}

class MoodService:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            print("WARNING: GEMINI_API_KEY not found in environment.")
            self.model = None
        else:
            genai.configure(api_key=api_key)
            self.model = genai.GenerativeModel('gemma-3-27b-it')
            print(self.model)

    def detect_mood(self, user_text: str) -> Dict[str, Any]:
        """
        Determines the mood by combining heuristic keyword matching and AI classification.
        """
        user_text = user_text.lower()
        
        # 1. Try Heuristic Keywords first (Instant & Predictable)
        heuristic_key = self.heuristic_detect_mood(user_text)
        if heuristic_key:
            print("h")
            return MOOD_CATEGORIES[heuristic_key]

        # 2. Fallback to AI if no strong keyword matches
        if self.model:
            print("model")
            categories_str = ", ".join(MOOD_CATEGORIES.keys())
            prompt = f"""
            Analyze the following text and classify it into exactly ONE of these categories: {categories_str}.
            Text: "{user_text}"
            
            Return ONLY the category name in lowercase. If unsure, return 'chill'.
            """
            try:
                response = self.model.generate_content(prompt)
                detected_key = response.text.strip().lower()
                if detected_key in MOOD_CATEGORIES:
                    return MOOD_CATEGORIES[detected_key]
            except Exception as e:
                print(f"Error in Gemini Mood Detection: {e}")

        # 3. Final Fallback: Random Vibe (keeps it fresh)
        random_key = random.choice(list(MOOD_CATEGORIES.keys()))
        print("rand")
        return MOOD_CATEGORIES[random_key]

    def heuristic_detect_mood(self, user_text: str) -> str:
        """
        Simple keyword scoring to find the best matching mood category.
        """
        scores = {key: 0 for key in MOOD_CATEGORIES.keys()}
        
        for key, config in MOOD_CATEGORIES.items():
            for keyword in config["keywords"]:
                if keyword in user_text:
                    scores[key] += 1
        
        # Find the category with the highest score
        best_mood = max(scores, key=scores.get)
        if scores[best_mood] > 0:
            return best_mood
        
        return None

    def get_playlist_name(self, mood_label: str, user_text: str) -> str:
        """
        Generates a creative playlist name using AI if available.
        """
        if not self.model:
            return f"{mood_label} Mix"

        prompt = f"""
        Generate a creative, catchy, and short playlist name (max 3 words) 
        for a {mood_label} mood based on this user description: "{user_text}".
        Example: "3AM Thoughts", "Neon Dreams", "Sun-Drenched Beats".
        Return ONLY the name.
        """
        
        try:
            response = self.model.generate_content(prompt)
            return response.text.strip()
        except:
            return f"{mood_label} Mix"

# Singleton instance
mood_service = MoodService()
