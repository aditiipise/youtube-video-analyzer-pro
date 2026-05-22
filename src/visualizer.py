import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("youtube_data.csv")

titles = df["Title"]
views = df["Views"]

plt.figure(figsize=(10,5))

plt.bar(titles, views)

plt.xticks(rotation=45)

plt.xlabel("Video Titles")
plt.ylabel("Views")
plt.title("YouTube Video Views Analysis")

plt.tight_layout()

plt.show()