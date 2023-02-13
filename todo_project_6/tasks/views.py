from django.shortcuts import render, redirect

from .forms import TaskForm,TagForm
# Create your views here.
from .models import Task, Tag
from django.contrib.auth.decorators import login_required
@login_required(login_url='login')
def add_task(request):
    if request.method=="POST":
        form=TaskForm(data=request.POST)
        form.instance.user=request.user
        if form.is_valid():
            new_task=form.save()
            return  redirect('dashboard')
    else:
        form=TaskForm()
    #after the validation if the form is correct it will redirect to the task
    #if not that if render same html page by default filled fields and error for the field which is mistake
    return  render(request,"tasks/add_task.html",{
            'form':form
        })

@login_required(login_url='login')
def add_tag(request):
    if request.method=='POST':
        form=TagForm(data=request.POST)
        form.instance.user = request.user
        if form.is_valid():
            tag=form.save()
            return redirect('dashboard')
    else:
        form=TagForm()
    return render(request,'tasks/add_tag.html',{
            'form':form
        })
