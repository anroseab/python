from django.shortcuts import render
from . models import *
# Create your views here.
def index(request):
    context={}
    
    obj=Packages.objects.all()
    context['obj']=obj
    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')
def packages(request):
    context={}
    
    obj=Packages.objects.all()
    context['obj']=obj
    return render(request,'packages.html',context)
def test(request):
    return render(request,'test.html')
def gallery(request):
    return render(request,'gallery.html')
def department(request):
    return render(request,'department.html')
def contact(request):
    return render(request,'contact.html')
def branch(request):
    return render(request,'branch.html')
def appointment(request):
    return render(request,'appointment.html')
def blog(request):
    return render(request,'blog.html')
def subblog(request):
    return render(request,'subblog.html')
def subpackage(request):
    context={}
    
    sub=Subpackage.objects.all()
    obj=Packages.objects.all()
    context['obj']=obj
    context['sub']=sub
    return render(request,'subpackage.html',context)