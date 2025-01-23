from django.contrib import admin
from django.contrib.auth.models import Group, Permission
from .models import User, Profile

# Unregister the default Group model
admin.site.unregister(Group)

# Custom admin class for the Group model
class CustomGroupAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Display the name of the group
    search_fields = ('name',)  # Add a search bar for group names
    filter_horizontal = ('permissions',)  # Easier management of permissions in the admin

# Register models with customizations
admin.site.register(Profile)
admin.site.register(Group, CustomGroupAdmin)
admin.site.register(Permission)

