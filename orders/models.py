from django.db import models
from users.models import User
from django.conf import settings  
from drugs.models import Drug  

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    drug = models.ForeignKey(Drug, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, choices=[('Pending', 'Pending'), ('Shipped', 'Shipped'), ('Delivered', 'Delivered')], default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.drug.name} x {self.quantity}"

    def save(self, *args, **kwargs):
        self.total_price = self.quantity * self.drug.price  # Assuming Drug has a 'price' field
        super().save(*args, **kwargs)
