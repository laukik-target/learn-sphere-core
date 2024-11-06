from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    # Fields to display in the admin list view
    list_display = ('username', 'email', 'name', 'mobile', 'is_admin', 'is_student', 'is_staff', 'is_superuser')
    
    # Fields to filter by in the admin list view
    list_filter = ('is_admin', 'is_student', 'is_staff', 'is_superuser')
    
    # Fields to search by in the admin list view
    search_fields = ('username', 'email', 'name', 'mobile')
    
    # Fields to display on the user detail page
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('name', 'mobile', 'is_admin', 'is_student')}),
    )
    
    # Fields required for creating a new user
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('name', 'mobile', 'is_admin', 'is_student')}),
    )

admin.site.register(User, CustomUserAdmin)
