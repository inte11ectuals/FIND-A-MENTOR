

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.urls import reverse

#tasks = ["saad","khan","king","qwert"]
#creating form using django

class Newtaskform(forms.Form):
   task=forms.CharField(label="new task")
  # priority=forms.IntegerField(label="pri",min_value=1,max_value=7)
 
#     Create your views here.
def task(request):
   if "tasks" not in request.session:
      request.session["tasks"] =[]

   #doing server side validation
   if request.method == "POST":
      form = Newtaskform(request.POST)
      if form.is_valid():
         new_task = form.cleaned_data["task"]
         #tasks.append(new_task)
         request.session["tasks"] += [new_task]
         return HttpResponseRedirect(reverse("mentor_links:tasks"))
      else:
         return render (request,"main_web/tasks.html",{
            "old_form":form,
            #"tasks":tasks
         })


   return render(request,"main_web/tasks.html",{
      "k":["khan","saad","lol"],
      #"tasks":tasks,
      "forms_by_django":Newtaskform(),
      "tasks":request.session["tasks"],
   })


def index(request):
   if "tasks" not in request.session:
      request.session["tasks"] =[]

   #return HttpResponse("hello, world")
   return render(request, "main_web/index.html",{
      
      "tasks":request.session["tasks"],
   })

def greet(request,name):
   #return HttpResponse(f"hello, {name.capitalize()} ")
   return render(request,"main_web/layout.html",{
   "name":name.capitalize() ,
   })

def home(request):
   return render(request, "main_web/home.html")


