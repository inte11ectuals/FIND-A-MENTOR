from asyncio import tasks
from unicodedata import name
from django.urls import path
from . import views


app_name="tasks" #uniquly identifies these urls

urlpatterns = [
   path("",views.index,name="index"),
   
   #path("<str:name>", views.greet,name="greet"),  #adding a genral url
   
   path("task",views.task,name="tasks")

]