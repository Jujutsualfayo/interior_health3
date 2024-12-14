from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Order
from drugs.models import Drug
from django.contrib.auth.decorators import login_required
from django.db import transaction

@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'orders/order_list.html', {'orders': orders})

@login_required
@transaction.atomic
def place_order(request, drug_id):
    drug = get_object_or_404(Drug, id=drug_id)
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 0))
        if quantity <= 0:
            messages.error(request, 'Quantity must be greater than 0.')
        elif quantity > drug.stock_quantity:
            messages.error(request, 'Insufficient stock.')
        else:
            total_price = drug.price * quantity
            Order.objects.create(
                user=request.user,
                drug=drug,
                quantity=quantity,
                total_price=total_price
            )
            drug.stock_quantity -= quantity
            drug.save()
            messages.success(request, 'Order placed successfully!')
            return redirect('orders:order_list')
    return render(request, 'orders/place_order.html', {'drug': drug})

@login_required
def order_detail(request, pk):
    order = get_object_or_404(Order, id=pk, user=request.user)
    return render(request, 'orders/order_detail.html', {'order': order})

@login_required
def cancel_order(request, pk):
    order = get_object_or_404(Order, id=pk, user=request.user)
    if request.method == 'POST':
        order.delete()
        messages.success(request, 'Order canceled successfully.')
        return redirect('orders:order_list')
    return render(request, 'orders/cancel_order.html', {'order': order})
