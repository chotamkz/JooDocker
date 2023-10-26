from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('projects/', views.get_projects, name='projects'),
    path('projects-create/', views.create_project, name='create-project'),
    path('projects-update/<id>', views.update_project, name='update-project'),
    path('projects-delete/<id>', views.delete_project, name='delete-project'),
    path('login/', views.login_page, name='loginBase'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.register, name='registerBase')
]
