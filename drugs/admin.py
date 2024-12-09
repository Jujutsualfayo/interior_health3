from django.contrib import admin
from .models import Drug

class DrugAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock_quantity', 'expiry_date')
    search_fields = ('name', 'category', 'manufacturer')
    list_filter = ('category', 'expiry_date')
    ordering = ('name',)

# Register the Drug model with the custom admin
admin.site.register(Drug, DrugAdmin)
