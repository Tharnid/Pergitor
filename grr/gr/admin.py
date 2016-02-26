from django.contrib import admin
from gr.models import Gr

# Register your models here.

class GrAdmin(admin.ModelAdmin):
    pass

admin.site.register(Gr, GrAdmin)
