
from django.db import models

import django.contrib.auth.models  # importing authentable users table from posgresql, fyam_database

# Create your models here.

class University(models.Model):
   id = models.AutoField(primary_key=True,null=False)
   name=models.CharField(max_length=30)
   location=models.CharField(max_length=100)


class Gikians(models.Model):
   reg_no=models.IntegerField(primary_key=True )
  
   id=models.ForeignKey(University,null=False,on_delete=models.CASCADE,to_field='id')
  
   username=models.CharField(max_length=50,unique=True,null=False)
   hash = models.CharField(max_length=100,unique=True,null=False)
   email=models.EmailField(unique=True,null=False)
   name=models.CharField(max_length=20)
   year=models.IntegerField(unique=True,null=False)
   faculty=models.CharField(max_length=10)

   # class Meta:
   #    verbose_name_plural = 'Gikians'


   def __int__(self):
       return self.reg_no

class Giki_societis(models.Model):
   reg_no=models.ForeignKey(Gikians,null=False,on_delete=models.CASCADE,primary_key=True,to_field='reg_no')
   socities = models.CharField(max_length=30)


class Giki_teams(models.Model):
   reg_no=models.ForeignKey(Gikians,null=False,on_delete=models.CASCADE,primary_key=True)
   teams = models.CharField(max_length=30)


class Mentor(models.Model):
   reg_no=models.ForeignKey(Gikians,null=False,on_delete=models.CASCADE, related_name='%(class)s_regno_derived_from_Gikians_Model',primary_key=True)

   year=models.ForeignKey(Gikians,null=False,on_delete=models.CASCADE, related_name='%(class)s_year_derived_from_Gikians_model',to_field='year')

   def __str__(self) :
       return self.reg_no

class Mentees(models.Model):
   reg=models.ForeignKey(Gikians,on_delete=models.CASCADE, related_name='%(class)s_reg_derived_from_Gikian_models',primary_key=True)

   mentor_id=models.ForeignKey(Mentor,null=False,on_delete=models.CASCADE)
   
   year = models.ForeignKey(Gikians,null=False,on_delete=models.CASCADE,to_field='year')

class Mentees_of_mentors(models.Model):
   reg=models.ForeignKey(Mentor,on_delete=models.CASCADE,primary_key=True)

   men_id=models.ForeignKey(Mentees,null=False,on_delete=models.CASCADE,to_field='reg')

class Mentor_skills(models.Model):
   reg=models.ForeignKey(Mentor,on_delete=models.CASCADE,primary_key=True,to_field='reg_no')
   skills=models.CharField(max_length=40)

class Mentor_best_courses(models.Model):
   reg=models.ForeignKey(Mentor,on_delete=models.CASCADE,primary_key=True,to_field='reg_no')
   best_courses=models.CharField(max_length=40)



class Mentee_weak_courses(models.Model):
   reg=models.ForeignKey(Mentees,on_delete=models.CASCADE,primary_key=True,to_field='reg')
   weak_courses=models.CharField(max_length=40)

class Mentee_interests(models.Model):
   reg=models.ForeignKey(Mentees,on_delete=models.CASCADE,primary_key=True,to_field='reg')
   interests = models.CharField(max_length=40)

   












