"""helloworld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('my-groups/', views.my_groups),
    path('my-groups/<groupname>', views.get_one_group),
    path('get-random-group/', views.get_random_group),
    path('unfollow/<groupname>', views.unfollow),
    path('see-groups/', views.see_groups),
    path('groups/', views.get_groups, name='groups'),
    path('create-groups/', views.create_group, name='create-groups'),
    path('update-groups/<id>', views.update_groups, name='update-groups'),
    path('delete-groups/<id>', views.delete_groups, name='delete-groups'),
    path('login/', views.loginpage, name='loginkz'),
    path('register/', views.registerpage, name='registerkz'),
    path('logout/', views.logoutUser, name='logoutkz')
]
