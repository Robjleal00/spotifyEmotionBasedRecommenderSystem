import spotipy 
from spotipy.oauth2 import SpotifyClientCredentials 
from dotenv import load_dotenv, dotenv_values
import os

load_dotenv()

# Initialize Spotify client
client_credentials_manager = SpotifyClientCredentials(client_id=os.getenv("SPOTIPY_CLIENT_ID"), client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"))
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Define a function to get mood-based playlists or tracks
def get_mood_based_music(mood):
    # Use Spotify's search functionality to find playlists or tracks related to the mood
    results = sp.search(q=mood, type='playlist,track')
    
    # Process the results and return relevant information
    # For example, you might want to extract track names, artists, etc.

    # Print results 
    print(results)


# Example usage
mood = 'happy'
get_mood_based_music(mood)


