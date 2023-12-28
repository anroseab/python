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

admin.site.register(Packages,Packages_display)
admin.site.register(Blog,Blog_display)
admin.site.register(Contact,Contact_display)
admin.site.register(Enquiry,Enquiry_display)
