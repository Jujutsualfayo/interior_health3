from django.shortcuts import render, redirect
from .models import Order
from drugs.models import Drug

def order_list(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'orders/order_list.html', {'orders': orders})

def place_order(request, drug_id):
    drug = Drug.objects.get(id=drug_id)
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity'))
        total_price = drug.price * quantity
        Order.objects.create(
            user=request.user,
            drug=drug,
            quantity=quantity,
            total_price=total_price
        )
        return redirect('orders:order_list')
    return render(request, 'orders/place_order.html', {'drug': drug})

