from django.contrib import admin
from .models import Drug

# Register the Drug model with the Django admin interface
@admin.register(Drug)
class DrugAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'manufacturer', 'price', 'stock_quantity', 'expiry_date')
    search_fields = ('name', 'category', 'manufacturer')
    list_filter = ('category', 'manufacturer')
    ordering = ('name',)

