from django.contrib import admin
from . models import *
# Register your models here.
class Packages_display(admin.ModelAdmin):
    list_display=['image','description']
class Blog_display(admin.ModelAdmin):
    list_display=['image','description']

class Contact_display(admin.ModelAdmin):
    list_display=['name','email','phone','message','subject']

class Enquiry_display(admin.ModelAdmin):
    list_display=['name','email','phone','message']

class Appointment_display(admin.ModelAdmin):
    list_display=['name','email','phone','message','age','gender','address','date','time']

class Sub_package_display(admin.ModelAdmin):
    list_display=['name','test1','test2','test3','test4','test5','cost','image']




admin.site.register(Packages,Packages_display)
admin.site.register(Blog,Blog_display)
admin.site.register(Contact,Contact_display)
admin.site.register(Enquiry,Enquiry_display)
admin.site.register(Appointment,Appointment_display)
admin.site.register(Sub_package,Sub_package_display)
