from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserChangeForm
# Create your views here.

def index(request):
    form=UserChangeForm(request.POST)

    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request,'index.html',{'form':form})
def home(request):
    return render(request,'home.html')