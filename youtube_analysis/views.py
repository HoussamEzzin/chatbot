from django.shortcuts import render
import json
from youtube_analysis.ytb_analyse import get_video_data
from django.views.generic.base import TemplateView
from django.views.generic import View
from django.http import JsonResponse, response
# Create your views here.


def home(request):
    return render(request, 'youtube_analysis/home.html')

class AnalyzeVideo(TemplateView):
    template_name = 'youtube_analysis/video_analyze.html'
    
    
class AnalyzeVideoApi(View):
    def post(self,request,*args,**kwargs):
        
        input_data = json.loads(request.body.decode('utf-8'))

        
        if 'text' not in input_data:
            return JsonResponse({
                'text':[
                    'The attribute "text" is required.'
                ]
            },status=400)
        

        print('Request : ', request)
        print('********Input is :', input_data)
        data = get_video_data()
        print(data)
        response_data = {
            'test' : 'nothing for now..'
        }
        return JsonResponse(response_data, status=200,safe=False)

    def get(self, request, *args, **kwargs):
        data = get_video_data()
        return JsonResponse({
            'data': data
        })

    