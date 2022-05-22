from django.contrib import admin

from .models import Gikians,University

# Register your models here.

class Gikian_admin(admin.ModelAdmin):
   list_display=(
      'reg_no','id','username','hash','email','name','year','faculty'
   )

admin.site.register(Gikians,Gikian_admin)
admin.site.register(University)


