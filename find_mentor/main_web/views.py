from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
   #return HttpResponse("hello, world")
   return render(request, "main_web/index.html")

def greet(request,name):
   #return HttpResponse(f"hello, {name.capitalize()} ")
   return render(request,"main_web/layout.html",{
   "name":name.capitalize() ,
   })


