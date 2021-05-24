from pytube import YouTube

link = input(" Enter the link of youtube video you want to download: ")
yt = YouTube(link)

ys = yt.streams.get_highest_resolution()

print(" Downloading.....")
ys.download()
print('Download completed!!!!')
