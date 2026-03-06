# JSON Response Schema

This is the contract between the Backend and Frontend for the recommendation response.

## Schema Definition

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "VibeRecommendationResponse",
  "type": "object",
  "required": ["mood", "playlist_name", "recommendations"],
  "properties": {
    "mood": {
      "type": "object",
      "required": ["label", "color_hex"],
      "properties": {
        "label": {
          "type": "string",
          "description": "The AI-detected mood name.",
          "example": "Late Night 🌙"
        },
        "color_hex": {
          "type": "string",
          "description": "The hex code for the UI theme shift.",
          "example": "#1A1A2E"
        }
      }
    },
    "playlist_name": {
      "type": "string",
      "description": "A creative name generated for the vibe.",
      "example": "3AM Thoughts"
    },
    "recommendations": {
      "type": "array",
      "minItems": 3,
      "maxItems": 5,
      "items": {
        "type": "object",
        "required": ["title", "artist"],
        "properties": {
          "title": { "type": "string" },
          "artist": { "type": "string" },
          "spotify_url": { "type": "string", "format": "uri" },
          "vibe_snippet": { 
            "type": "string", 
            "description": "A short blurb why this fits the mood." 
          }
        }
      }
    }
  }
}
```

## Example Payload

```json
{
  "mood": {
    "label": "Late Night 🌙",
    "color_hex": "#1A1A2E"
  },
  "playlist_name": "3AM Thoughts",
  "recommendations": [
    {
      "title": "Nights",
      "artist": "Frank Ocean",
      "spotify_url": "https://open.spotify.com/track/7ccv9_example",
      "vibe_snippet": "Gliding through the quiet hours."
    },
    {
      "title": "After Dark",
      "artist": "Mr.Kitty",
      "spotify_url": "https://open.spotify.com/track/2_example",
      "vibe_snippet": "Dark synth for midnight drives."
    },
    {
      "title": "Space Song",
      "artist": "Beach House",
      "spotify_url": "https://open.spotify.com/track/7_example",
      "vibe_snippet": "Weightless and nostalgic."
    }
  ]
}
```
