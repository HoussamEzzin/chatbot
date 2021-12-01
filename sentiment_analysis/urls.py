from sentiment_analysis import views
from django.urls import path
from sentiment_analysis.views import ChatterBotApiView, ChatterBotAppView

urlpatterns = [
    path('',views.sentiment_analysis_home, name='sentiment-analysis'),
    path('sentiment-analysis-chat/api/', ChatterBotApiView.as_view(),name='sentiment-chat' ),
    path('sentiment-analysis-chat/',ChatterBotAppView.as_view(),name ='sentiment-analysis-chat'),
]
