from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# Create your views here.


def loginS(request):
    return render(request, 'base/loginBase.html')


def get_projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'base/projects.html', context)


@login_required(login_url='login')
def create_project(request):
    form = ProjectForm()
    #print(request.POST)
    #project = Project()
    if request.method == 'POST':
        #print(request.POST['name'])
        #project.name = request.POST['name']
        #project.description = request.POST['description']
        #user = User()
        #project.save()
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form': form}
    return render(request, 'base/project_form.html', context)


@login_required(login_url='login')
def update_project(request, id):
    project = Project.objects.get(id=id)
    form = ProjectForm(instance=project)

    if request.user != project.creater_id:
        return HttpResponse('You doesnt have root')

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form': form}
    return render(request, 'base/project_update.html', context)


@login_required(login_url='login')
def delete_project(request, id):
    project = Project.objects.get(id=id)

    if request.user != project.creater_id:
        return HttpResponse('You doesnt have root')

    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {'project': project}
    return render(request, 'base/project_delete.html', context)


def login_page(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Invalid data')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('projects')
        else:
            messages.error(request, 'username or password incorrect')
    context = {}
    return render(request, 'base/loginBase.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def register(request):
    user = UserCreationForm()
    if request.method == 'POST':
        user = UserCreationForm(request.POST)
        if user.is_valid():
            user.save()
            return redirect('login')
        else:
            messages.error(request, 'An error occurred while register')
    context = {'user': user}
    return render(request, 'base/registerBase.html', context)
