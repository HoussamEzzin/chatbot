from django.urls import path
from youtube_analysis.views import AnalyzeVideo, AnalyzeVideoApi
from youtube_analysis import views
from django.conf.urls import url

urlpatterns = [
    path('', views.home,name='youtube-analysis-home-page'),
    path('analyze-video/',AnalyzeVideo.as_view(), name="analyze-video"),
    path('analyze-video/api/', AnalyzeVideoApi.as_view(), name="analyze-video-api")

]