#spotify api
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

#spotify api stuffs
client_credentials_manager = SpotifyClientCredentials(client_id='4b871fb41ea44c80a85c1f2b5dca02c4', client_secret='72403b95666847bea30098434bb2b046')
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

feild = sp.me()
print(feild)

# for a in sp.current_user_playlists(limit=50, offset=0):
#     print(a)
#lkjdfnhjkjn