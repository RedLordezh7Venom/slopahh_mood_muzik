import requests
import json

BASE_URL = "http://localhost:8000/api/v1"

def test_recommendation_flow():
    print("--- Testing /api/v1/recommend ---")
    payload = {
        "text_input": "I am feeling really energetic and ready to party",
        "mood_id": None
    }
    
    try:
        response = requests.post(f"{BASE_URL}/recommend", json=payload)
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            
            # Verify mood detection
            mood = data.get("mood", {})
            print(f"Detected Mood: {mood.get('label')} ({mood.get('color_hex')})")
            
            # Verify playlist name
            playlist_name = data.get("playlist_name")
            print(f"Playlist Name: {playlist_name}")
            
            # Verify songs count
            recommendations = data.get("recommendations", [])
            print(f"Songs Count: {len(recommendations)}")
            
            for i, song in enumerate(recommendations, 1):
                print(f"  {i}. {song['title']} - {song['artist']} ({song['album']})")
            
            assert len(recommendations) == 3, "Should return exactly 3 songs"
            assert playlist_name is not None, "Playlist name should be generated"
            assert mood.get("label") is not None, "Mood should be detected"
            
            return True
        else:
            print(f"Error: {response.text}")
            return False
    except Exception as e:
        print(f"Connection Failed: {e}")
        return False

def test_history_storage():
    print("\n--- Testing /api/v1/history ---")
    try:
        response = requests.get(f"{BASE_URL}/history")
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            history = response.json()
            print(f"History Record Count: {len(history)}")
            
            if len(history) > 0:
                latest = history[0]
                print(f"Latest Entry: {latest['detected_mood']} - {latest['playlist_name']}")
                return True
            else:
                print("No history records found.")
                return False
        else:
            print(f"Error: {response.text}")
            return False
    except Exception as e:
        print(f"Connection Failed: {e}")
        return False

if __name__ == "__main__":
    success_rec = test_recommendation_flow()
    if success_rec:
        test_history_storage()
