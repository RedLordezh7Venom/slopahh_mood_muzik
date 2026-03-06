import random

SONG_LIBRARY = {
    "late_night": [
        {"title": "Nights", "artist": "Frank Ocean", "album": "Blonde", "spotify_url": "https://open.spotify.com/track/7ccv9"},
        {"title": "After Dark", "artist": "Mr.Kitty", "album": "Time", "spotify_url": "https://open.spotify.com/track/2"},
        {"title": "The Less I Know The Better", "artist": "Tame Impala", "album": "Currents", "spotify_url": "https://open.spotify.com/track/6P93"},
        {"title": "Space Song", "artist": "Beach House", "album": "Depression Cherry", "spotify_url": "https://open.spotify.com/track/7"},
        {"title": "Starboy", "artist": "The Weeknd", "album": "Starboy", "spotify_url": "https://open.spotify.com/track/7MX"},
        {"title": "Self Control", "artist": "Frank Ocean", "album": "Blonde", "spotify_url": "https://open.spotify.com/track/5"},
        {"title": "Sweater Weather", "artist": "The Neighbourhood", "album": "I Love You.", "spotify_url": "https://open.spotify.com/track/2"}
    ],
    "gym": [
        {"title": "Metamorphosis", "artist": "INTERWORLD", "album": "Metamorphosis", "spotify_url": "https://open.spotify.com/track/2"},
        {"title": "Till I Collapse", "artist": "Eminem", "album": "The Eminem Show", "spotify_url": "https://open.spotify.com/track/4"},
        {"title": "MURDER IN MY MIND", "artist": "KORDHELL", "album": "MURDER IN MY MIND", "spotify_url": "https://open.spotify.com/track/1"},
        {"title": "Can't Be Touched", "artist": "Roy Jones Jr.", "album": "Body Head Bangerz", "spotify_url": "https://open.spotify.com/track/3"},
        {"title": "POWER", "artist": "Kanye West", "album": "My Beautiful Dark Twisted Fantasy", "spotify_url": "https://open.spotify.com/track/2"},
        {"title": "X Gon' Give It To Ya", "artist": "DMX", "album": "Cradle 2 the Grave", "spotify_url": "https://open.spotify.com/track/1"},
        {"title": "Lose Yourself", "artist": "Eminem", "album": "8 Mile", "spotify_url": "https://open.spotify.com/track/7"}
    ],
    "focus": [
        {"title": "Experience", "artist": "Ludovico Einaudi", "album": "In a Time Lapse", "spotify_url": "https://open.spotify.com/track/1"},
        {"title": "Gymnopédie No. 1", "artist": "Erik Satie", "album": "3 Gymnopédies", "spotify_url": "https://open.spotify.com/track/5"},
        {"title": "Cornfield Chase", "artist": "Hans Zimmer", "album": "Interstellar", "spotify_url": "https://open.spotify.com/track/6"},
        {"title": "Time", "artist": "Hans Zimmer", "album": "Inception", "spotify_url": "https://open.spotify.com/track/3"},
        {"title": "Avril 14th", "artist": "Aphex Twin", "album": "Drukqs", "spotify_url": "https://open.spotify.com/track/2"},
        {"title": "Day One", "artist": "Hans Zimmer", "album": "Interstellar", "spotify_url": "https://open.spotify.com/track/4"},
        {"title": "River Flows In You", "artist": "Yiruma", "album": "First Love", "spotify_url": "https://open.spotify.com/track/6"}
    ],
    "nostalgic": [
        {"title": "Dreams", "artist": "Fleetwood Mac", "album": "Rumours", "spotify_url": "https://open.spotify.com/track/0"},
        {"title": "Everybody Wants To Rule The World", "artist": "Tears For Fears", "album": "Songs From The Big Chair", "spotify_url": "https://open.spotify.com/track/4"},
        {"title": "Mr. Brightside", "artist": "The Killers", "album": "Hot Fuss", "spotify_url": "https://open.spotify.com/track/0"},
        {"title": "Slide", "artist": "Goo Goo Dolls", "album": "Dizzy Up the Girl", "spotify_url": "https://open.spotify.com/track/0"},
        {"title": "Wonderwall", "artist": "Oasis", "album": "(What's the Story) Morning Glory?", "spotify_url": "https://open.spotify.com/track/7"},
        {"title": "Yellow", "artist": "Coldplay", "album": "Parachutes", "spotify_url": "https://open.spotify.com/track/3"},
        {"title": "Fast Car", "artist": "Tracy Chapman", "album": "Tracy Chapman", "spotify_url": "https://open.spotify.com/track/2"}
    ],
    "heartbreak": [
        {"title": "Someone Like You", "artist": "Adele", "album": "21", "spotify_url": "https://open.spotify.com/track/4"},
        {"title": "Drivers License", "artist": "Olivia Rodrigo", "album": "SOUR", "spotify_url": "https://open.spotify.com/track/2"},
        {"title": "Self Control", "artist": "Frank Ocean", "album": "Blonde", "spotify_url": "https://open.spotify.com/track/5"},
        {"title": "Liability", "artist": "Lorde", "album": "Melodrama", "spotify_url": "https://open.spotify.com/track/6"},
        {"title": "Skinny Love", "artist": "Bon Iver", "album": "For Emma, Forever Ago", "spotify_url": "https://open.spotify.com/track/0"},
        {"title": "Glimpse of Us", "artist": "Joji", "album": "SMITHEREENS", "spotify_url": "https://open.spotify.com/track/6"},
        {"title": "Traitor", "artist": "Olivia Rodrigo", "album": "SOUR", "spotify_url": "https://open.spotify.com/track/5"}
    ],
    "chill": [
        {"title": "Passionfruit", "artist": "Drake", "album": "More Life", "spotify_url": "https://open.spotify.com/track/5"},
        {"title": "Sundress", "artist": "A$AP Rocky", "album": "Sundress", "spotify_url": "https://open.spotify.com/track/2"},
        {"title": "Coffee", "artist": "Miguel", "album": "Wildheart", "spotify_url": "https://open.spotify.com/track/0"},
        {"title": "Telepatía", "artist": "Kali Uchis", "album": "Sin Miedo", "spotify_url": "https://open.spotify.com/track/6"},
        {"title": "Location", "artist": "Khalid", "album": "American Teen", "spotify_url": "https://open.spotify.com/track/1"},
        {"title": "Better Together", "artist": "Jack Johnson", "album": "In Between Dreams", "spotify_url": "https://open.spotify.com/track/4"},
        {"title": "Wait a Minute!", "artist": "Willow", "album": "ARDIPITHECUS", "spotify_url": "https://open.spotify.com/track/0"}
    ]
}

def get_songs_by_vibe(mood_key: str, count: int = 3):
    """
    Retrieves a random selection of songs matching the provided mood category.
    """
    available_songs = SONG_LIBRARY.get(mood_key, SONG_LIBRARY["chill"])
    return random.sample(available_songs, min(len(available_songs), count))

def generate_yt_link(title: str, artist: str):
    """
    Generates a YouTube search link for the given song and artist.
    """
    query = f"{artist} {title}".replace(" ", "+")
    return f"https://www.youtube.com/results?search_query={query}"
