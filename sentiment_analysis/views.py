from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import json
from django.views.generic.base import TemplateView
from django.views.generic import View
from django.http import JsonResponse, response
from chatterbot import ChatBot
from chatterbot.ext.django_chatterbot import settings
from chatterbot.trainers import ChatterBotCorpusTrainer
from sentiment_analysis.analyze import analyze_input, determine_emotion
# Create your views here.


score = 0
count = 0

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
        global count
        
        input_data = json.loads(request.body.decode('utf-8'))
        
        
    
        
        
        if 'text' not in input_data:
            return JsonResponse({
                'text':[
                    'The attribute "text" is required.'
                ]
            },status=400)
        
        response = self.chatterbot.get_response(input_data)
        response_data = response.serialize()
        
        
       
        print('**Success response is :', response_data)
        

        while count <3 :
            count +=1
            print('MESSAGE NUMBER ', count)
            score = analyze_input(input_data['text'],score)
            print('----SCORE IS : ', score)
            print("****////***** EMOTION IS :", determine_emotion(score))
            if count == 3:
                emotion_data = {
                    'emotion' : determine_emotion(score),
                    'close_chat' : 'true'
                }
                return JsonResponse(emotion_data, status=200,safe=False)
            return JsonResponse(response_data, status=200,safe=False)
       
        
    
    def get(self, request, *args, **kwargs):
        return JsonResponse({
            'name': self.chatterbot.name
        })