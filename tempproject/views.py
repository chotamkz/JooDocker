from django.shortcuts import render

friendslist = [
    {
        'id': 1,
        'firstname': 'Daniyar',
        'lastname': 'Nurlanov',
        'gender': 'male'
    },
    {
        'id': 2,
        'firstname': 'Chotam',
        'lastname': 'DonerLong',
        'gender': 'male'
    },
    {
        'id': 3,
        'firstname': 'asdfsd',
        'lastname': 'asdfasdfafdasdf',
        'gender': 'male'
    }
]

subjectlist = [
    {
        'id': 1,
        'name': "DBMS2",
        'instructor': 'Maxat Skakov'
    },
    {
        'id': 2,
        'name': "Algo2",
        'instructor': 'Dauren Ayazbayev'
    },
    {
        'id': 3,
        'name': "English",
        'instructor': 'Zere Kukayeva'
    }
]


def index(request):
    context = {'friends': friendslist}
    return render(request, 'tempproject/friends.html', context)


def subjects(request):
    context = {'subjects': subjectlist}
    return render(request, 'tempproject/subjects.html', context)
