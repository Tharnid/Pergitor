from django.contrib import admin
from gr.models import Gr

# Register your models here.

class GrAdmin(admin.ModelAdmin):
    # admin screen
    list_display = ('text', 'created_on', 'total_likes')
    list_filter = ['created_on']
    search_fields = ['text']

admin.site.register(Gr, GrAdmin)
