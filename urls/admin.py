from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    list_display = ('display_name', 'is_staff')
    search_fields = ('display_name',)
    ordering = ('display_name',)

admin.site.register(User, CustomUserAdmin)
