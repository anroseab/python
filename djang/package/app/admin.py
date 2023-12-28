from django.contrib import admin
from .models import *
# Register your models here.
class pk(admin.ModelAdmin):
    list_display=['name']

class kp(admin.ModelAdmin):
    list_display=['name','package']



admin.site.register(Package,pk)
admin.site.register(Sub_package,kp)