import json
import random



def generate():
    #returns a list [comment,author]
    quotes = open('chatbot/data/quotes.json')
    quotes_data = json.load(quotes)
    comment_data = []
    i = random.randint(0,len(quotes_data))
    comment_data.append(quotes_data[i]['text'])
    comment_data.append(quotes_data[i]['author'])
    quotes.close()
    return comment_data