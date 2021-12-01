from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import json
from django.views.generic.base import TemplateView
from django.views.generic import View
from django.http import JsonResponse, response
from chatterbot import ChatBot
from chatterbot.ext.django_chatterbot import settings
from chatterbot.trainers import ChatterBotCorpusTrainer
# Create your views here.

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

score = 0
analyze = True

@login_required(login_url='/login')
def sentiment_analysis_home(request):
    return render(request, 'sentiment_analysis/home.html' )


class ChatterBotAppView(TemplateView):
    template_name = 'sentiment-analysis-chat.html'


class ChatterBotApiView(View):
    chatterbot = ChatBot(**settings.CHATTERBOT)
    trainer = ChatterBotCorpusTrainer(chatterbot)
    
   
    try :
        trainer.train("sentiment_analysis/data/sentiments.yml")
        print('sentiment training completed !')
    except Exception:
        print('ERRO WITH TRAINING !')
        
    
    
    
    
    def post(self,request,*args,**kwargs):
        global score
        global analyze
        input_data = json.loads(request.body.decode('utf-8'))
        
        
        
        if analyze == True : 
            words = input_data['text'].split(' ')
            for word in words:
                if word in positive_words and word not in ['',' ']:
                    score += 1
                elif word in negative_words and word not in ['',' ']:
                    score -= 1
            print('Actual Score : '+str(score)+'\n\n')
            if score >= 10:
                analyze = False
                print('Great !')
            elif score <= -10 :
                analyze = True
                print('Terrible')
    
      
        
        if 'text' not in input_data:
            return JsonResponse({
                'text':[
                    'The attribute "text" is required.'
                ]
            },status=400)
        
        response = self.chatterbot.get_response(input_data)
        response_data = response.serialize()
        
        
       
        print('**Success response is :', response_data)
        
        emotion = 'nothing'
        output_result = [response_data,emotion]
       
        return JsonResponse(output_result, status=200,safe=False)
    
    def get(self, request, *args, **kwargs):
        return JsonResponse({
            'name': self.chatterbot.name
        })