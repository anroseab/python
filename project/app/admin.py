from django.contrib import admin
from . models import *
# Register your models here.
class Packages_display(admin.ModelAdmin):
    list_display=['image','description']
class Subpackage_display(admin.ModelAdmin):
    list_display=['image','description','test1','test2','test3','test4','test5','cost']





admin.site.register(Packages,Packages_display)
admin.site.register(Subpackage,Subpackage_display)
