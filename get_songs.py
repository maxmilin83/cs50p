from pytube import Playlist


def returnList(url):
    continued={}
    playlist = Playlist(url)

    songs = []

    for video in playlist.videos:
      index = list(playlist.videos).index(video)

      try:
        # Video was not continued
        songs.append(video.title)
      except:
        continued[index] = 1
        continue

    for i in continued:
      try:
        songs.append(playlist.videos[i].title)
      except:
        continue

    return songs



