from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import tooo
from todo import models
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def signup(req):
    if req.method == 'POST':
        fnm=req.POST.get('fnm')
        emailid=req.POST.get('email')
        pwd=req.POST.get('pwd')
        print(fnm,emailid,pwd)
        my_user=User.objects.create_user(fnm,emailid,pwd)
        my_user.save()
        return redirect('login')
    return render(req,'signup.html')

def login_View(req):
    if req.method=='POST':
        fnm = req.POST.get('fnm')
        pwd=req.POST.get('pwd')
        print(fnm,pwd)
        user = authenticate(req,
        username=fnm,
        password=pwd
        )
        if user is not None:
            login(req,user)
            return redirect('todo')
        else:
             return render(req, 'login.html', {
        'error': 'Invalid username or password'
    })
    return render(req,'login.html')


@login_required   
def todo_view(req):
    if req.method == 'POST':
        title = req.POST.get('title')
        print(title)

        obj = models.tooo(
            title=title,
            user=req.user
        )
        obj.save()

    tasks = tooo.objects.filter(user=req.user)

    return render(req, 'todo.html', {
        'tasks': tasks
    })



def delete_task(req, id):
    task = tooo.objects.get(srno=id)
    task.delete()
    return redirect('todo')    



def edit_task(req, id):

    task = tooo.objects.get(srno=id)

    if req.method == 'POST':
        task.title = req.POST.get('title')
        task.save()
        return redirect('todo')

    return render(req, 'update.html', {
        'task': task
    })    





def logout_view(request):
    logout(request)
    return redirect('login')  # login page par redirect