from youtube_transcript_api import YouTubeTranscriptApi
from textblob import TextBlob

text = []
start_dates = []
duration = []


def get_text_from_video(video_key):
    srt = YouTubeTranscriptApi.get_transcript(video_key)  #You can get key from link add this feature

    for i in range(0,len(srt)):
        dict(srt[i])
        text.append((srt[i]["text"]))
        start_dates.append((srt[i]["start"]))
        duration.append((srt[i]["duration"]))
    
    for line in text:
        print(line)
        analysis = TextBlob(line)
        print(analysis.sentiment) #Polarity how positive or negative sentiment, #Subjectivity how much opinion on it

    

data_youtube = get_text_from_video("youtube_video_key")

