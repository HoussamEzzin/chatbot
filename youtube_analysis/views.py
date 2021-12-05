from django.shortcuts import render
import json
from youtube_analysis.ytb_analyse import get_video_data, analyze_input, determine_emotion
from django.views.generic.base import TemplateView
from django.views.generic import View
from django.http import JsonResponse
# Create your views here.

score = 0

def home(request):
    return render(request, 'youtube_analysis/home.html')

class AnalyzeVideo(TemplateView):
    template_name = 'youtube_analysis/video_analyze.html'
    
    
class AnalyzeVideoApi(View):
    def post(self,request,*args,**kwargs):
        global score
        
        input_data = json.loads(request.body.decode('utf-8'))

        
            
        
        if 'text' not in input_data:
            return JsonResponse({
                'text':[
                    'The attribute "text" is required.'
                ]
            },status=400)
        print(input_data['text'])
        input = input_data['text'].replace('https://www.youtube.com/watch?v=', '')
        
        
        print('Request : ', request)
        print('********Input is :', input_data)
        data = get_video_data(input)
        for d in data:
            print(d['snippet']['topLevelComment']
                        ['snippet']['textOriginal'])
            score = analyze_input(d['snippet']['topLevelComment']
                        ['snippet']['textOriginal'],score)
        print('************ ACUTAL SCORE : ', score)
        response_data = {
            'emotion' : determine_emotion(score)
        }
        return JsonResponse(response_data, status=200,safe=False)

    def get(self, request, *args, **kwargs):
        data = get_video_data()
        return JsonResponse({
            'data': data
        })

    