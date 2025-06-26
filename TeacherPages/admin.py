from django.contrib import admin
from .models import Teacher

# Register your models here.

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')
    search_fields = ('username', 'email')
    list_filter = ('username', 'email')

admin.site.register(Teacher, TeacherAdmin)
