from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def get_friends(request):
    friends_list = ["Danik", "Damir", "DDD", "Alisher"]
    return HttpResponse(friends_list)


def get_one_friend(request, friendname):
    friends_list = ["Danik", "Damir", "DDD", "Alisher"]
    if friendname in friends_list:
        return HttpResponse(friendname)
    return HttpResponse('You have not such friend')


def index(request):
    return HttpResponse('To get a friends list, you should add /my-friends into url')