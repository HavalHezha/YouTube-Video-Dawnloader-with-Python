from pytube import YouTube
from sys import argv

print()

path = input("place ")
link = argv[1]
yt = YouTube(link)

print(yt.title)
print(yt.views)
print(yt.author)
print(yt.publish_date)

yd = yt.streams.get_highest_resolution()
yd.download(path)
