from googleapiclient.discovery import build
import random
import webbrowser

DEVELOPER_KEY = ''   #Hier Developer_Key einfügen
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

prefix = ['']      #Wenn ihr was Spezial suchen wolt einfach Prefix und Postfix ausfüllen sonst frei lassen
postfix = ['']

def youtube_search():
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
    search_response = youtube.search().list(
        q=random.choice(prefix) + str(random.randint(999, 9999)) + random.choice(postfix),
        part='snippet',
        maxResults=5
    ).execute()

    videos = []

    for search_result in search_response.get('items', []):
        if search_result['id']['kind'] == 'youtube#video':
            videos.append('%s' % (search_result['id']['videoId']))
    return random.choice(videos)  # Zufälliges Video auswählen

def open_youtube_video(video_id):
    url = f"https://www.youtube.com/watch?v={video_id}"
    webbrowser.open(url)

if __name__ == "__main__":
    video_id = youtube_search()  # Zufällige YouTube-Video-ID abrufen
    open_youtube_video(video_id)  # YouTube-Video im Webbrowser öffnen