from django.urls import path
from todo_list import views
from todo_list.views import ChatterBotAppView,ChatterBotApiView

urlpatterns = [
    path('', views.home,name='to-do-home-page'),
    path('todo-list-chat/', ChatterBotAppView.as_view(),name='todo-list-chat'),
    path('todo-list-chat/api', ChatterBotApiView.as_view(),name='todo-list-api'),
]