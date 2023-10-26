import random

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Group
from .forms import GroupFrom
from django.contrib import messages


def my_groups(request):
    listOfGroups = ['Tengrinews', 'AlmatyToday', 'SDU.kz', 'News']
    return HttpResponse(listOfGroups)


def get_one_group(request, groupname):
    listOfGroups = ['Tengrinews', 'AlmatyToday', 'SDU.kz', 'News']
    if groupname in listOfGroups:
        return HttpResponse(groupname)
    return HttpResponse('You doesn’t follow this group')


def get_random_group(request):
    listOfGroups = ['Tengrinews', 'AlmatyToday', 'SDU.kz', 'News']
    return HttpResponse(random.choice(listOfGroups))


def unfollow(request, groupname):
    listOfGroups = ['Tengrinews', 'AlmatyToday', 'SDU.kz', 'News']
    listOfGroups.remove(groupname)
    return HttpResponse(listOfGroups)


groupslist = [
    {
        'id': 1,
        'name': 'Tengrinews'
    },
    {
        'id': 2,
        'name': 'KTK'
    },
    {
        'id': 3,
        'name': 'AlmatyToday'
    },
    {
        'id': 4,
        'name': 'Newskz'
    }

]


def see_groups(request):
    context = {'groups': groupslist}
    return render(request, 'groups/groups.html', context)


@login_required(login_url='login')
def create_group(request):
    form = GroupFrom()
    if request.method == 'POST':
        form = GroupFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('groups')
    context = {'form': form}
    return render(request, 'groups/group_form.html', context)


def get_groups(request):
    groups = Group.objects.all()
    context = {'groups': groups}
    return render(request, 'groups/groups.html', context)


@login_required(login_url='login')
def update_groups(request, id):
    group = Group.objects.get(id=id)
    form = GroupFrom(instance=group)
    if request.user != group.creator_id:
        return HttpResponse('You doesnt have root')
    if request.method == 'POST':
        form = GroupFrom(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return redirect('groups')
    context = {'form': form}
    return render(request, 'groups/group-update.html', context)


@login_required(login_url='login')
def delete_groups(request, id):
    group = Group.objects.det(id=id)

    if request.user != group.creater_id:
        return HttpResponse('You doesnt have root')
    if request.method == 'POST':
        group.delete()
        return redirect('groups')
    context = {'group': group}
    return render(request, 'groups/group-delete.html', context)


def loginpage(request):
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
            return redirect('groups')
        else:
            messages.error(request, 'username or password incorrect')
        context = {}
        return render(request, 'groups/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def registerpage(request):
    user = UserCreationForm()
    if request.method == 'POST':
        user = UserCreationForm(request.POST)
        if user.is_valid():
            user.save()
            return redirect('login')
        else:
            messages.error(request, 'An error occurred while register')
    context = {'user': user}
    return render(request, 'groups/register.html', context)