from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from .models import Profile

# Get the custom User model
User = get_user_model()

# Unregister the default User model
admin.site.unregister(User)

# Custom admin class for the User model
class CustomUserAdmin(DefaultUserAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active')  # Customize fields in list view
    search_fields = ('username', 'email')  # Add search bar for username and email
    ordering = ('username',)  # Order users by username

# Register the custom User admin
admin.site.register(User, CustomUserAdmin)

# Unregister the default Group model
admin.site.unregister(Group)

# Custom admin class for the Group model
class CustomGroupAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Display the name of the group
    search_fields = ('name',)  # Add a search bar for group names
    filter_horizontal = ('permissions',)  # Easier management of permissions in the admin

# Register other models with customizations
admin.site.register(Profile)
admin.site.register(Group, CustomGroupAdmin)
admin.site.register(Permission)
