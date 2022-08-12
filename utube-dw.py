

import pytube

yt = pytube.YouTube("https://www.youtube.com/watch?v=dBKicoI8CUI")
videos = yt.streams.all()

print("videos", videos)
