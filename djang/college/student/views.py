from django.shortcuts import render
# from django.http import HttpResponse
from . models import *
# Create your views here.

def index(request):
    student=Student.objects.all()
    teacher=Teacher.objects.all()
    batch=Batch.objects.all()
    return render(request,'index.html',{'student':student,'teacher':teacher,'batch':batch})