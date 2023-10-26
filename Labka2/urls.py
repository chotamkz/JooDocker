from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('base/', views.page_menu),
    path('book-search/<nameOfBooks>', views.book_search1),
    path('book-search/', views.book_search2),
    path('books/', views.get_books, name='books'),
    path('books/<int:pk>', views.get_books_detail, name='books'),
]

