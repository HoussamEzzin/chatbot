from django.urls import path
from . import views
from django.conf.urls import url
from chatbot.views import ChatterBotApiView, ChatterBotAppView

urlpatterns = [
    path('', views.home_page,name='home-page')
]