from flask import Flask, render_template, request
from googleapiclient.discovery import build

app = Flask(__name__)

API_KEY = 'AIzaSyBeuBps7xrMnwyKKtgljHoaXLvdJrlz0V0'

@app.route('/', methods=['GET', 'POST'])
def index():
    videos = []
    if request.method == 'POST':
        keyword = request.form['keyword']
        videos = search_youtube_videos(keyword)
    return render_template('index.html', videos=videos)

def search_youtube_videos(keyword):
    youtube = build('youtube', 'v3', developerKey=API_KEY)
    search_response = youtube.search().list(
        q=keyword,
        type='video',
        part='id,snippet',
        maxResults=10  # total pencarian
    ).execute()

    videos = []
    for search_result in search_response.get('items', []):
        video_data = {
            'title': search_result['snippet']['title'],
            'description': search_result['snippet']['description'],
            'video_id': search_result['id']['videoId'],
            'thumbnail_url': search_result['snippet']['thumbnails']['default']['url']
        }
        videos.append(video_data)

    return videos


if __name__ == '__main__':
    app.run(debug=True)
