from django.contrib import admin
from .models import User, Profile
from django.contrib.auth.models import Group, Permission
from .models import User

admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Group)
admin.site.register(Permission)

