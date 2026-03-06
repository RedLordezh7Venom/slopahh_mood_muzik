# API Specification: Mood-Based Music Recommender

This document defines the RESTful endpoints used by the frontend to communicate with the FastAPI backend.

## Base URL
`http://localhost:8000/api/v1`

---

## 🚀 Endpoints

### 1. Get Recommendations
The core endpoint that translates a user's vibe into a music selection.

*   **URL**: `/recommend`
*   **Method**: `POST`
*   **Request Body**:
    ```json
    {
      "text_input": "it's raining outside and i'm feeling a bit melancholy but cozy",
      "mood_id": null  // Optional: Used if selecting a predefined card instead of typing
    }
    ```
*   **Response Structure (200 OK)**:
    ```json
    {
      "request_id": "uuid-v4",
      "detected_mood": {
        "label": "Post-Rain Nostalgia",
        "vibe_color": "#4A90E2",
        "tags": ["lofi", "melancholy", "cozy"]
      },
      "playlist_name": "3AM Thoughts",
      "recommendations": [
        {
          "id": 1,
          "title": "Nights",
          "artist": "Frank Ocean",
          "album_art": "https://example.com/art.jpg",
          "spotify_url": "https://open.spotify.com/track/...",
          "preview_url": "https://example.com/preview.mp3",
          "vibe_description": "Perfect for late night introspection."
        },
        ...
      ]
    }
    ```

---

### 2. List Predefined Moods
Used to populate the "Quick Selection" cards on the home screen.

*   **URL**: `/moods`
*   **Method**: `GET`
*   **Response Structure (200 OK)**:
    ```json
    [
      { "id": "late-night", "label": "Late Night 🌙", "default_color": "#121212" },
      { "id": "gym", "label": "Power Hour 🔥", "default_color": "#FF4500" },
      { "id": "focus", "label": "Deep Focus 🧠", "default_color": "#2E8B57" }
    ]
    ```

---

### 3. Get User Mood History (Bonus)
Retrieves the user's last 10 entries.

*   **URL**: `/history`
*   **Method**: `GET`
*   **Response Structure (200 OK)**:
    ```json
    [
      {
        "timestamp": "2026-03-06T05:10:00Z",
        "input": "coding all night",
        "detected_mood": "Deep Focus"
      },
      ...
    ]
    ```

---

### 4. Health Check
Internal check for monitoring and Docker orchestration.

*   **URL**: `/health`
*   **Method**: `GET`
*   **Response structure**:
    ```json
    { "status": "healthy", "service": "slopahh_muzik_backend" }
    ```

## 🛠️ Error Handling

| Code | Meaning | Description |
| :--- | :--- | :--- |
| `400` | Bad Request | Missing `text_input` or invalid JSON. |
| `422` | Validation Error | Input text is too long (over 500 chars). |
| `500` | Internal Error | AI service is down or Database connectivity issue. |
