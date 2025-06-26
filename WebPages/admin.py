from django.contrib import admin
from .models import User

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'isAdmin')
    search_fields = ('username', 'email', 'isAdmin')
    list_filter = ('username', 'email', 'isAdmin')

admin.site.register(User, UserAdmin)
