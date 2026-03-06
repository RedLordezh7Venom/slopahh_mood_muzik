import random

# Prefix bank categorized by vibe
PREFIXES = {
    "late_night": ["3AM", "Midnight", "Lunar", "Dark", "Sleepless", "Quiet", "Neon"],
    "gym": ["Main Character", "Alpha", "Hyper", "Power", "Beast", "Iron", "Victory"],
    "focus": ["Deep", "Zen", "Neural", "Digital", "Office", "Flow", "Mindful"],
    "nostalgic": ["Rewind", "80s", "Childhood", "Vintage", "Golden", "Retro", "Old-School"],
    "heartbreak": ["Blue", "Lonely", "Broken", "Rainy", "Empty", "Bitter", "Stormy"],
    "chill": ["Coastal", "Beach", "Golden Hour", "Lazy", "Soft", "Mellow", "Summer"]
}

# Suffix bank for creative flair
SUFFIXES = ["Energy", "Dreams", "Vibes", "Thoughts", "Beats", "Notes", "Echoes", "Moments", "Chronicles", "Waves"]

def generate_playlist_name(mood_key: str) -> str:
    """
    Randomly combines a mood-specific prefix with a creative suffix.
    """
    prefix_list = PREFIXES.get(mood_key, PREFIXES["chill"])
    
    prefix = random.choice(prefix_list)
    suffix = random.choice(SUFFIXES)
    
    return f"{prefix} {suffix}"
