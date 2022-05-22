from asyncio import tasks
from unicodedata import name
from django.urls import path,include
from . import views



app_name="mentor_links" #uniquly identifies these urls
urlpatterns = [
   path("home_api",views.home_api,name="index"),
   path("",views.index,name="index"),
   
   #path("<str:name>", views.greet,name="greet"),  #adding a genral url
   
   path("task",views.task,name="tasks"),

   path("home",views.home,name="home"),
   path("task",views.task,name="uni"),
   path("task",views.task,name="mentors"),
   path("task",views.task,name="reviews"),
   path("task",views.task,name="about"),
   path("task",views.task,name="signup"),



]