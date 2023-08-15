from pytube import Playlist

#playlist link to download goes here
playlist = Playlist('')

#shows in the terminal how many videos are in the playlist
print('Number of videos in playlist: %s' % len(playlist.video_urls))

# Loop through all videos in the playlist and download them to the root folder
for video in playlist.videos:
    stream = video.streams.filter(only_audio=True).first().download()
    
#shows when the process has completed
print('done')