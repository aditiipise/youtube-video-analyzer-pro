from googleapiclient.discovery import build
import pandas as pd
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import API_KEY

youtube = build('youtube', 'v3', developerKey=API_KEY)

request = youtube.search().list(
    part='snippet',
    q='Python programming',
    maxResults=5
)

response = request.execute()
video_data = []

for item in response['items']:
    title = item['snippet']['title']
    channel = item['snippet']['channelTitle']

    print("Title:", title)
    print("Channel:", channel)
    print("-" * 50)

    if 'videoId' in item['id']:
        video_id = item['id']['videoId']

    video_request = youtube.videos().list(
        part="statistics",
        id=video_id
    )

    video_response = video_request.execute()

    if len(video_response['items']) > 0:
        stats = video_response['items'][0]['statistics']

        views = stats.get('viewCount', '0')
        likes = stats.get('likeCount', '0')
        comments = stats.get('commentCount', '0')

        print("Views:", views)
        print("Likes:", likes)
        print("Comments:", comments)
        video_data.append({
    "Title": title,
    "Channel": channel,
    "Views": views,
    "Likes": likes,
    "Comments": comments
})
        print("=" * 50)

video_request = youtube.videos().list(
    part="statistics",
    id=video_id
)

video_response = video_request.execute()

stats = video_response['items'][0]['statistics']

views = stats.get('viewCount', '0')
likes = stats.get('likeCount', '0')
comments = stats.get('commentCount', '0')

print("Views:", views)
print("Likes:", likes)
print("Comments:", comments)
print("=" * 50)
df = pd.DataFrame(video_data)

df.to_csv("youtube_data.csv", index=False)

print("CSV file saved successfully!")