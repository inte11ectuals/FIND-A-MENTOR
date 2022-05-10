from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
   path("",views.index,name="index"),
   #adding a genral url
   path("<str:name>", views.greet,name="greet")

]