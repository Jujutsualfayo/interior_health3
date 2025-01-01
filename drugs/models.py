from django.db import models

class Drug(models.Model):
    # Drug information
    name = models.CharField(max_length=200, unique=True)
    category = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    manufacturer = models.CharField(max_length=200)
    expiry_date = models.DateField(null=True, blank=True)  # Allow NULL for expiry_date

    # Inventory management
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField(default=0)
    minimum_stock = models.PositiveIntegerField(default=10)

    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def is_low_stock(self):
        """Check if the stock is below the minimum level."""
        return self.stock_quantity < self.minimum_stock
