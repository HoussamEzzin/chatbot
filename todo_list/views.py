from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import json
from django.views.generic.base import TemplateView
from django.views.generic import View
from django.http import JsonResponse
from chatterbot import ChatBot
from chatterbot.ext.django_chatterbot import settings
from chatterbot.trainers import ChatterBotCorpusTrainer
# Create your views here.

@login_required(login_url='/login')
def home(request):
    return render(request,'todo_list/home.html')


class ChatterBotAppView(TemplateView):
    template_name = 'todo_list_chat.html'


class ChatterBotApiView(View):
    chatterbot = ChatBot(**settings.CHATTERBOT)
    trainer = ChatterBotCorpusTrainer(chatterbot)

    try :
        trainer.train("todo_list/data/todo.yml")
        print('sentiment training completed !')
    except Exception:
        print('ERROR WITH TRAINING !')
        

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
   
        print('**Success response is :', response_data)
    
        return JsonResponse(response_data, status=200,safe=False)
       
        
    
    def get(self, request, *args, **kwargs):
        return JsonResponse({
            'name': self.chatterbot.name
        })
