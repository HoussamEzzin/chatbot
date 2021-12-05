# Intializing positive and negative words array for sentiment analysis using rule-based approach

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

def analyze_input(input,previous_score):
    words = input.split(' ')
    
    for word in words:
        if word in positive_words and word not in ['',' ']:
            previous_score += 1
        elif word in negative_words and word not in ['',' ']:
            previous_score -= 1
    
    return previous_score

def determine_emotion(score):
    emotion = ''
    if score >= 10:
        emotion = 'Happy'
    elif score > 0 and score < 10 :
        emotion = 'Good'
    elif score < 0 and score > -10 :
        emotion = 'not very well'
    else:
        emotion = 'feeling terrible'
    
    emotion = 'You are ' + emotion
    
    return emotion



    
    
            