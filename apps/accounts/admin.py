from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['username', 'email', 'display_name', 'profile_picture', 'banner', 'bio']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('display_name', 'profile_picture', 'banner', 'bio')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('display_name', 'profile_picture', 'banner', 'bio')}),
    )

admin.site.register(User, CustomUserAdmin)