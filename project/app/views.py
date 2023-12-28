from django.shortcuts import render,redirect
from . models import *
# Create your views here.
def index(request):
    context={}
    
    obj=Packages.objects.all()
    context['obj']=obj
    if request.method=='POST':
          name=request.POST.get('name')
          email=request.POST.get('email')
          phone=request.POST.get('phone')
          message=request.POST.get('message')
          
          if request.POST:
               details=Enquiry.objects.create(name=name,email=email,phone=phone,message=message)
               details.save()
               return redirect('index')

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
    if request.method=='POST':
          name=request.POST.get('name')
          email=request.POST.get('email')
          phone=request.POST.get('phone')
          subject=request.POST.get('subject')
          message=request.POST.get('message')
     
          if request.POST:
               details=Contact.objects.create(name=name,email=email,phone=phone,subject=subject,message=message)
               details.save()
               return redirect('contact')

    return render(request,'contact.html')
def branch(request):
    return render(request,'branch.html')
def appointment(request):
    return render(request,'appointment.html')
def blog(request):
    context={}
          
    m=Blog.objects.all()
    context['m']=m

    return render(request,'blog.html',context)
def subblog(request):
    return render(request,'subblog.html')
def subpackage(request):
    context={}
    
    obj=Packages.objects.all()
    context['obj']=obj
    return render(request,'subpackage.html',context)