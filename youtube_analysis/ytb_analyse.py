# Intializing positive and negative words array for sentiment analysis using rule-based approach
from googleapiclient.discovery import build
positive_words = []
with open('sentiment_analysis/data/positive.txt') as p :
    for line in p:
        line = line.strip()
        positive_words.append(line)

negative_words = []
with open('sentiment_analysis/data/negative.txt') as n:
    for line in n:
        line = line.strip()
        negative_words.append(line)

import time


# YOUTUBE_DEVELOPER_KEY = 'AIzaSyD2-CXZu9MJ04hX6-dYohzaFvCBzmsSpWo'
# YOUTUBE_CLIENT_ID = '35225584560-o2p8e71k47b9ks892gmssk7jbrskrrvv.apps.googleusercontent.com'
youTubeApiKey = 'AIzaSyD2-CXZu9MJ04hX6-dYohzaFvCBzmsSpWo'
youtube=build('youtube','v3',developerKey=youTubeApiKey)
# channelId='ooZ98n-ZDUA'

def analyze_input(input,previous_score):
    words = input.split(' ')
    
    for word in words:
        if word in positive_words and word not in ['',' ']:
            previous_score += 1
        elif word in negative_words and word not in ['',' ']:
            previous_score -= 1
    
    return previous_score

def get_video_data(video_id):
    # statdata=youtube.channels().list(part='snippet',id=channelId).execute()
    request = youtube.commentThreads().list(
                    part="snippet,replies",
                    videoId = video_id
        )
    response = request.execute()
    data = response['items']  
    return data

def determine_emotion(score):
    emotion = ''
    if score >= 10:
        emotion = 'Awesome !!'
    elif score > 0 and score < 10 :
        emotion = 'Good'
    elif score < 0 and score > -10 :
        emotion = 'not very well'
    else:
        emotion = 'really terrible'
    
    emotion = 'This video is ' + emotion
    
    return emotion

