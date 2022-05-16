import youtube_dl
import queue
import threading

# Constants
PLAYLIST_URL = "" # insert playlist URL here
threads_to_start = 10

video_queue = queue.Queue()

ydl_opts = {
    'outtmpl': 'downloads/%(title)s.%(ext)s',
    'writesubtitles': False,
    'format': "bestaudio/best",
    'writethumbnail': False,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

ydl = youtube_dl.YoutubeDL(ydl_opts)

# Extracts the URL of each individual video from the playlist info.
def extract_video_urls(url):
    video_urls = []

    ie_result = ydl.extract_info(url, False)

    if 'entries' in ie_result:
        videos = ie_result['entries']
        for i, item in enumerate(videos):
            try:
                url = videos[i]['webpage_url']
            except Exception as e:
                print(f"Skipping extracting video, failed with exception: {e}")

            video_urls.append(url)
            video_queue.put(url)

        return video_urls
    else:
        print("Playlist is empty or the URL entered is invalid")
        return []

def download_single_video(url):
    print(f"Downloading the following video: {url}")
    ydl.download([url])

def worker():
    while not video_queue.empty():
        url = video_queue.get()
        try:
            download_single_video(url)
        except Exception as e:
            print(f"Failed to download video {url} with exception: {e}")
        video_queue.task_done()

extract_video_urls(PLAYLIST_URL)

for i in range(threads_to_start):
    t = threading.Thread(target=worker, daemon=True) # daemon means that all threads will exit when the main thread exits
    t.start()

video_queue.join()