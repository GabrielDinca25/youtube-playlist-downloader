# youtube-playlist-downloader
Simple  Windows multithreaded Youtube .mp3 python playlist downloader

Currently, the playlist provded must not contain any age-restricted or deleted videos.

Prerequisites:

- Install Python

- Run 'pip install yt-dlp' in cmd (the pip command can be found in your Python installation folder under the Scripts directory, if it's missing 'run python -m ensurepip --default-pip')

- Run 'pip install phantomjs'

- Add the ffmpeg folder found in this repo to your PATH environment variable.

Use: 

- Open the playlister.py file and set the PLAYLIST_URL constant to the URL of the playlist that you want to download. (TO-DO: pass the URL as a command line parameter)
- Run the playlister.py script (E.g.: python.exe playlister.py)


