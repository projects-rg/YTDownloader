from pytube import YouTube

#link to the single video to download
yt = YouTube('link')

#prints the name of the single video
print("Title: ", yt.title)


yd = yt.streams.get_audio_only()

# ADD FOLDER HERE / Savees to root folder
yd.download()

#shows when the process has completed
print('done')