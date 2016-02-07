from django.contrib import admin
# import book object
from .models import Author, Book


# Register your models here.
admin.site.register(Book)
admin.site.register(Author)
