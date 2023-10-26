from django.urls import path
from . import views

urlpatterns = [
    path('my-friends', views.index),
    path('my-subjects', views.subjects)
]