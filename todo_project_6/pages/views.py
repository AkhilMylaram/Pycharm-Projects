from django.shortcuts import render, redirect
from pages import  urls
from tasks.models import Task, Tag
from django.contrib.auth.decorators import  login_required
# Create your views here.


from .forms import  ContactForm

def contact(request):
    if request.method=="POST":
        form=ContactForm(data=request.POST)
        if form.is_valid():
            #send email
            return redirect('tasks')
    else:
        form=ContactForm()
    return render(request,'pages/contact.html',{
            'form':form
        })

@login_required(login_url='login') #who ever comes to this view they should login if they are not logged in they need to redict
def dashboard(request):                #redirect them to login url

    user=request.user
    tasks=user.task_set.all()
    tags=user.tag_set.all()
    return render(request,'pages/dashboard.html',{
        'tasks':tasks,
        'tags':tags
    })


