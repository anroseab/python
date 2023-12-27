from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')
def packages(request):
    return render(request,'packages.html')
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
    return render(request,'subpackage.html')