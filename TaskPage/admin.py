from django.contrib import admin
from .models import Task

# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ('taskID', 'title', 'createdBy', 'teacherName')
    search_fields = ('taskID', 'title', 'createdBy', 'teacherName')
    list_filter = ('taskID', 'title', 'createdBy', 'teacherName')

admin.site.register(Task, TaskAdmin)
