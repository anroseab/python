from django.shortcuts import render
from . models import *
from . form import *
# Create your views here.


def index(request):
    context={}
    st=Student.objects.all()
    st_form=St_form()
    if request.method=='POST':
        if 'save' in request.POST:
            st_form=St_form(request.POST)
            st_form.save()
        elif 'delete' in request.POST:
            key=request.POST.get('delete')
            st_del=Student.objects.get(id=key)
            st_del.delete()
        elif 'edit' in request.POST:
            key=request.POST.get('edit')
            st_edit=Student.objects.get(id=key)
            st_form=St_form(instance=st_edit)
    context['st']=st
    context['st_form']=st_form
    return render(request,'index.html',context)