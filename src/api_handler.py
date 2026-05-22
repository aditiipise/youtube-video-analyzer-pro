from googleapiclient.discovery import build

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import API_KEY
youtube = build('youtube', 'v3', developerKey=API_KEY)

request = youtube.search().list(
    part="snippet",
    q="Python programming",
    maxResults=5
)

response = request.execute()

for item in response['items']:
    print(item['snippet']['title'])