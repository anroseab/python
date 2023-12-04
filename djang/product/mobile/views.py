from django.shortcuts import render
from .  models import *
# Create your views 
def index(request):
    vivo=Vivo.objects.all()
    return render(request,'index.html',{'vivo':vivo})
