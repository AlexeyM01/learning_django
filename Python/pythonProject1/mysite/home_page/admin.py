from django.contrib import admin

# Register your models here.
from .models import *

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'experience', 'rating', 'photo')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')
    prepopulated_fields = ({"slug":('name',)})

admin.site.register(Teacher, TeacherAdmin)
