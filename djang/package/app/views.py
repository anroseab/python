from django.shortcuts import render
from . models import *

# Create your views here.
def index(request):
    context={}
    pkg=Package.objects.all()
    context['pkg']=pkg




    if request.method=='POST':
        obj=request.POST.get('package')
        print('object value is',obj)
        
        sub=Sub_package.objects.filter(package=obj)
        context['sub']=sub





    return render(request,'index.html',context)