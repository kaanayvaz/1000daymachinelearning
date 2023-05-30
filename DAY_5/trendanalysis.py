import httplib2
import requests

from bs4 import BeautifulSoup, SoupStrainer

url = "https://www.youtube.com/feed/trending" #Get trending video link

links = []
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

video_links = soup.find_all('a', {'class': 'yt-simple-endpoint style-scope ytd-video-renderer'})

# Extract the URLs from the links
video_urls = ['https://www.youtube.com' + link['href'] for link in video_links]

# Print the video URLs
for video_url in video_urls:
    print(video_url)

