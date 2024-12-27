from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Order
from drugs.models import Drug
from django.contrib.auth.decorators import login_required
from django.db import transaction

@login_required
def order_list(request):
    """View to list all orders made by the logged-in user."""
    orders = Order.objects.filter(user=request.user)
    return render(request, 'orders/order_list.html', {'orders': orders})

@login_required
@transaction.atomic
def place_order(request, drug_id=None):
    drug = get_object_or_404(Drug, id=drug_id) if drug_id else None

    if request.method == 'POST':
        selected_drug_id = request.POST.get('drug')
        quantity = int(request.POST.get('quantity', 0))
        drug = get_object_or_404(Drug, id=selected_drug_id) if not drug else drug

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

    drugs = Drug.objects.filter(stock_quantity__gt=0)
    return render(request, 'orders/place_order.html', {'drug': drug, 'drugs': drugs})

@login_required
@transaction.atomic
def cancel_order(request, pk):
    order = get_object_or_404(Order, id=pk, user=request.user)
    if request.method == 'POST':
        drug = order.drug
        if order.status != 'CANCELED':
            # Add back the quantity to the stock
            drug.stock_quantity += order.quantity
            drug.save()

        # Update the order's status to 'CANCELED' instead of deleting it
        order.status = 'CANCELED'
        order.save()

        messages.success(request, 'Order canceled successfully.')
        return redirect('orders:order_list')

    return render(request, 'orders/cancel_order.html', {'order': order})




@login_required
def order_detail(request, pk):
    """View to display details of a specific order."""
    order = get_object_or_404(Order, id=pk, user=request.user)
    return render(request, 'orders/order_detail.html', {'order': order})
