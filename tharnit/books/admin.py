from django.contrib import admin
# import book object
from .models import Book


# Register your models here.
admin.site.register(Book)
