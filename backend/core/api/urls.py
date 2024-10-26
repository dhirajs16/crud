from django.urls import path
from .views import *
urlpatterns = [
    path('books/', get_books, name='get_books'),
    path('create/', create_book, name='create_book'),
]