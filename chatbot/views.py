import chatterbot
from django.shortcuts import render
import json
from django.views.generic.base import TemplateView
from django.views.generic import View
from django.http import JsonResponse, response
from chatterbot import ChatBot
from chatterbot.ext.django_chatterbot import settings
from chatterbot.trainers import ChatterBotCorpusTrainer
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.
def home_page(request):
    
    return render(request, 'chatbot/home.html' )



# @login_required(login_url='/login')
class ChatterBotAppView(TemplateView):
    template_name = 'app.html'


class ChatterBotApiView(View):
    chatterbot = ChatBot(**settings.CHATTERBOT)
    trainer = ChatterBotCorpusTrainer(chatterbot)
    
    trainer.train("chatbot/data/train/train_tmp.yml")
    for i in range(1,29):
        try:
            train_path = "chatbot/data/train/train" + str(i) + ".yml"
            trainer.train(train_path)
        except Exception:
            print('---Rrror with train'+ str(i))
            continue
    
    try :
        trainer.train("chatbot/data/trainingdata.yml")
        
        trainer.train('chatterbot.corpus.english')
    except Exception:
        print('ERRO WITH TRAINING !')
        
    
    
    
    
    def post(self,request,*args,**kwargs):
        
        input_data = json.loads(request.body.decode('utf-8'))
        
        if 'text' not in input_data:
            return JsonResponse({
                'text':[
                    'The attribute "text" is required.'
                ]
            },status=400)
        
        response = self.chatterbot.get_response(input_data)
        response_data = response.serialize()
        print('Success response is :', response_data)
       
        return JsonResponse(response_data, status=200)
    
    def get(self, request, *args, **kwargs):
        return JsonResponse({
            'name': self.chatterbot.name
        })