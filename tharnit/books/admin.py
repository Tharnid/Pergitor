from django.contrib import admin
# import book object
from .models import Author, Book

# define book admin
class BookAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Book Details", {"fields": ["title", "authors"]}),
        ("Review", {"fields": ["is_favorite", "review", "date_reviewed"]}),
    ]

    readonly_fields = ("date_reviewed",)

    def book_authors(self, obj):
        return obj.list_authors()

    book_authors.short_description = "Author(s)"

    list_display = ("title", "book_authors", "date_reviewed", "is_favorite",)
    list_editable = ("is_favorite",)

# Register your models here.
admin.site.register(Author)
admin.site.register(Book, BookAdmin)
