from django.contrib import admin
from .models import Book

# Register your models here.
@admin.register(Book)
class BooksAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'release_year']