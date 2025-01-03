from django import template

register = template.Library()

@register.filter
def is_admin(user):
    """Check if the user belongs to the Admin group."""
    return user.groups.filter(name='Admin').exists()

@register.filter
def is_patient(user):
    """Check if the user belongs to the Patient group."""
    return user.groups.filter(name='Patient').exists()

