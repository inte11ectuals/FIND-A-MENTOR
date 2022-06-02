
# from crypt import methods

from ast import Pass
from asyncio.windows_events import NULL
from telnetlib import LOGOUT
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect

from django.urls import reverse
from rest_framework.parsers import JSONParser 
from django.http.response import JsonResponse
from .serializers import GikiansSerializer
from .models import Gikians
from django.db import models,connection
from django.db.models import Q
from . import models
from .forms import Newtaskform, Signupform
from django.contrib.auth import login, authenticate,logout 
from django.contrib import  messages 



#tasks = ["saad","khan","king","qwert"]

#     Create your views here.
def task(request):
   
   cursor = connection.cursor()
   try:
      cursor.execute('select * from main_web_gikians', ['localhost'])
      row = cursor.fetchall() 
   except Exception as e:
      cursor.close
   
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
      'users':row,
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


def home_api(request):
   if request.method=='GET':
      gikian=models.Gikians.objects.all()
      gikians_serializer=GikiansSerializer(gikian,many=True)
      return JsonResponse(gikians_serializer.data,safe=False)

#f'insert into main_web_gikians values({form.reg_no},{form.username},{form.password1},{form.email},concat({form.first_name},{form.last_name}),null,null,1)'

def signup(request):
  
   form = Signupform()

   if request.method=="POST":
      form = Signupform(request.POST)
      if form.is_valid():
         cursor = connection.cursor()
         try:
            cursor.execute('insert query into gikians table', ['localhost'])
            row = cursor.fetchall() 
            print(row)
         except Exception as e:
            cursor.close
        # print(form.password)
         messages.success(request,"The UserName or Password was Incorrect.")
         form.save()
      return redirect("/main_web/signin")
   else:
      form=Signupform()
   
   return render(request,"main_web/signup.html",{
      'form':form,
   })

def signin(request):
   
   if request.method=="POST": 
      username=request.POST['username']
      password=request.POST['password']
      
      user = authenticate(request,username=username,password=password)
       
      if user is not None:
         login(request, user)
         
         if request.user.is_superuser:
            user_dashboard_name=request.user.username
            
         elif not request.user.is_superuser:
            user_dashboard_name=request.user.username
           

         user_dashboard_name = username

         return redirect('/main_web/home')
         
      else:
         messages.success(request,"The UserName or Password was Incorrect.")
         return render(request,'registration/login.html')
   else:
      return render(request,"registration/login.html",{
      "status":"login" ,

      })

def signout(request):
   if request.method=="POST":
      a=logout(request)
      print(a)
      # return redirect('/main_web/home')
      return redirect("mentor_links:home")
   else:
      return render(request,"main_web/home.html")

gikian_map={'first'}

def dashboard(request):


   c1 = connection.cursor()
   c2 = connection.cursor()
   c3 = connection.cursor()
   c4 = connection.cursor()
   c5 = connection.cursor()
   c6 = connection.cursor()
   c7 = connection.cursor()
   c8 = connection.cursor()
   c9 = connection.cursor()
   c10 = connection.cursor()
   c11 = connection.cursor()
    
   try:
      c1.execute('select * from main_web_gikians', ['localhost'])
      c2.execute('select * from main_web_university',['localhost'])
      c3.execute('select * from main_web_giki_socities',['localhost'])
      c4.execute('select * from main_web_giki_teams',['localhost'])
      c5.execute('select * from main_web_mentor',['localhost'])
      c6.execute('select * from main_web_mentees_of_mentors',['localhost'])
      c7.execute('select * from main_web_mentor_skills',['localhost'])
      c8.execute('select * from main_web_mentor_best_courses',['localhost'])
      c9.execute('select * from main_web_mentees',['localhost'])
      c10.execute('select * from main_web_mentees_weak_courses',['localhost'])
      c11.execute('select * from main_web_mentee_interests',['localhost'])



      row1 = c1.fetchall() 
      row2 = c2.fetchall() 
      row3 = c3.fetchall() 
      row4 = c4.fetchall() 
      row5 = c5.fetchall() 
      row6 = c6.fetchall() 
      row7 = c7.fetchall() 
      row8 = c8.fetchall() 
      row9 = c9.fetchall() 
      row10 = c10.fetchall() 
      row11 = c11.fetchall() 

      

   except Exception as e:
      c1.close()
      c2.close()
      c3.close()
      c4.close()
      c5.close()
      c6.close()
      c7.close()
      c8.close()
      c9.close()
      c10.close()
      c11.close()
      
  
   context = {
               "table1":row1,
               "table2":row2,
               "table3":row3,
               "table4":row4,
               "table5":row5,
               "table6":row6,
               "table7":row7,
               "table8":row8,
               "table9":row9,
               "table10":row10,
               "table11":row11,

      }


   if request.user.is_superuser:

      user_dashboard_name = request.user.is_superuser

      print(f'{user_dashboard_name} is sueper user')
      return render(request,'main_web/admin_dashboard.html',context)
      

   elif not request.user.is_superuser:
      user_dashboard_name = request.user.is_superuser

      print(f'{user_dashboard_name} is not a sueper user')
      return render(request,'main_web/user_dashboard.html')
   else:
      return render(request,'main_web/home.html')