import requests
from urllib.parse import urlencode
import base64
import webbrowser
import json

client_id = "6b4eaabc0bd94e9fbc53eea5b1a4b753"
client_secret = "bd616f4ed50644129638ed09893a6732"
redirect_uri = "http://localhost:7777/callback"
code = "AQCDPMtnDpNG65z5SdH8zrrGX5J8L3_uak5fM2cOh8_RGyPz-lFVOUI_cCz_vuXsy1RR_KgQyYkCsgzys1gLfPKsO1r0pxSDoNlF5nh8IkX-_LPBIVS4I-l-i78uZNhRi2XKzuww7PNg9jBDptZd83ZQHBDnH6GcsKUQIyMXXwnAQHxLxwwhRNV8fc6qrol_ClRgFXyknMCWjw"

# URLS
auth_headers = {
    "client_id": client_id,
    "response_type": "code",
    "redirect_uri": redirect_uri,
    "scope": "playlist-modify-public"
}

#webbrowser.open("https://accounts.spotify.com/authorize?" + urlencode(auth_headers))


encoded_credentials = base64.b64encode(client_id.encode() + b':' + client_secret.encode()).decode("utf-8")

token_headers = {
    "Authorization": "Basic " + encoded_credentials,
    "Content-Type": "application/x-www-form-urlencoded"
}

token_data = {
    "grant_type": "authorization_code",
    "code": code,
    "redirect_uri": "http://localhost:7777/callback"
}

# r = requests.post("https://accounts.spotify.com/api/token", data=token_data, headers=token_headers)

# token = r.json()['access_token']
# print(token)

token='BQDWSUgSUk-VVBNQcUcRsReMV0QdAAYqCvvDYbpLDOkFRSnmANTl4NyQceGdLOt7PgAHnjSIGxUsoJDKaO4cxcoS6PZIfjfMb0yfs76SRJ4_XmRy3gXZ3h4k5PrUMpAIpOrlCzOQmE2repO2pEqAv50WClBjOIiu7jzct6VEaqLzuPgOgS6oejOQHI_zX3Uf-6R7PmTNfqOaYfu8SKNtHeo3YK_s-IE6THXMBaE'



#Create playlist
def createPlaylist(name):
    Header = {
            'Content-Type': 'application/json',
            "Authorization": "Bearer " + token,
            "scopes":"playlist-modify-public playlist-modify-private"
        }

    user_id = "31742hszjyu3ipwqzmmd5w4cm22e"
    endpoint_url = f"https://api.spotify.com/v1/users/{user_id}/playlists"
    request_body = json.dumps({
        "name":name
    })

    response = requests.post(endpoint_url,data = request_body,headers=Header)

    r = response.json()
    return [("Playlist created with the name "+ "'" + r['name'] +"' " +"Playlist ID: "+r['id']),r['id']]

#print(createPlaylist("test"))
#testID = '5SGvlrR5ElPEvcF4LzGdD2'

#Add songs to playlist
songs = ['spotify:track:5HCyWlXZPP0y6Gqq8TgA20','spotify:track:1KMkcUvF7m3SDChDOa7i5L']




def addSongs(playlistID,songs):

    endpoint_url = f"https://api.spotify.com/v1/playlists/{playlistID}/tracks"
    Header = {
            'Content-Type': 'application/json',
            "Authorization": "Bearer " + token,
            "scopes":"playlist-modify-public playlist-modify-private"
        }

    request_body = json.dumps({
        "uris":songs
    })

    response = requests.post(endpoint_url,data = request_body,headers=Header)
    return("Songs added to playlist with ID "+playlistID)






