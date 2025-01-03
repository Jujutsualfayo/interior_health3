from django import template

register = template.Library()

@register.filter(name='is_admin')
def is_admin(user):
    """Check if a user belongs to the 'Admin' group."""
    return user.groups.filter(name='Admin').exists()

