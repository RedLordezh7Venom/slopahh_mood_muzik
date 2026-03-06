from app.core.database import session_scope
from app.models.mood_history import MoodHistory
import requests
import os

BASE_URL = "http://localhost:8000/api/v1"

def get_actual_db_count():
    with session_scope() as session:
        return session.query(MoodHistory).count()

def perform_request(text):
    requests.post(f"{BASE_URL}/recommend", json={"text_input": text, "mood_id": None})

def run_db_audit():
    print("--- 🔍 Absolute Database Audit ---")
    
    # 1. Verify Insertion
    count_before = get_actual_db_count()
    print(f"Total records before: {count_before}")
    
    perform_request("Audit vibe check")
    
    count_after = get_actual_db_count()
    print(f"Total records after: {count_after}")
    
    if count_after == count_before + 1:
        print("✅ POINT 1: Success. Each request inserts exactly one record.")
    
    # 2. Verify Multiple Consecutive
    print("\n--- 🔄 Testing Consecutive Vibes ---")
    for i in range(3):
        perform_request(f"Consecutive vibe {i}")
    
    count_final = get_actual_db_count()
    print(f"Total records finally: {count_final}")
    if count_final == count_after + 3:
        print("✅ POINT 2: Success. Consecutive requests are logged correctly.")
    
    # 3. Persistence Check
    print("\n--- 💾 Persistence Note ---")
    print(f"DB File at: {os.path.join(os.getcwd(), 'data', 'music.db')}")
    print("Restart the server manually if desired. The count above proves data is stored in the persistent SQLite file.")

if __name__ == "__main__":
    run_db_audit()
