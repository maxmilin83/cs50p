import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

auth_manager = SpotifyClientCredentials(client_id='6b4eaabc0bd94e9fbc53eea5b1a4b753',client_secret='bd616f4ed50644129638ed09893a6732')
sp = spotipy.Spotify(auth_manager=auth_manager)


def getIds(songs):
    ids = []
    for i in songs:
        results = sp.search(q=i,limit=1,type='track')

        for track in results['tracks']['items']:
            ids.append('spotify:track:'+track['id'])

    return ids


