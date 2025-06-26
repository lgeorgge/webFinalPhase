from django.contrib import admin
from .models import Admin

# Register your models here.

class AdminAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')
    search_fields = ('username', 'email')
    list_filter = ('username', 'email')

admin.site.register(Admin, AdminAdmin)
