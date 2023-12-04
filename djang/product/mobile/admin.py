from django.contrib import admin
from . models import *
# Register your models here.
 

class Vivo_dis(admin.ModelAdmin):
    list_display=['name']

class Oppo_dis(admin.ModelAdmin):
    list_display=['name']

admin.site.register(Vivo,Vivo_dis)
admin.site.register(Oppo,Oppo_dis)


