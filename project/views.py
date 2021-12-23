from django.shortcuts import render, redirect
from .forms import CreateUserForm, TodoModelForm, UpdateTodoForm
from .models import TodoModel
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout

@login_required(login_url='login')
def index(request):
    model = TodoModel.objects.all()
    form = TodoModelForm()
    count_task = model.count()
    completed_task = TodoModel.objects.filter(complete=True)
    count_completed_task = completed_task.count()
    count_uncompleted_task = count_task - count_completed_task

    if request.method == 'POST':
        form = TodoModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = TodoModelForm()
    context = {'models':model, 'form': form, 'total': count_task, 'completed': count_completed_task, 'uncompleted': count_uncompleted_task}
    return render(request, 'index.html', context)


def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {'form': form}
    return render(request, 'register.html', context)

@login_required(login_url='login')
def delete(request, id):
    model = TodoModel(id=id)
    if request.method == 'POST':
        model.delete()
        return redirect('/')
    return render(request, 'delete.html', {})

@login_required(login_url='login')
def update(request, id):
    model = TodoModel.objects.get(id=id)
    form = UpdateTodoForm(request.POST or None, instance=model)
    if form.is_valid():
        form.save()
        return redirect('/')
    context = {'form': form}
    return render(request, 'update.html', context)

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credentials')
    context = {}
    return render(request, 'login.html', context)

def logout_page(request):
    logout(request)
    return redirect('/')
