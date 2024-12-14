from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Order
from drugs.models import Drug

def order_list(request):
    if not request.user.is_authenticated:  # Ensure the user is logged in
        messages.error(request, "You need to be logged in to view orders.")
        return redirect('users:login')
    orders = Order.objects.filter(user=request.user)
    return render(request, 'orders/order_list.html', {'orders': orders})

def place_order(request, drug_id):
    drug = get_object_or_404(Drug, id=drug_id)
    if request.method == 'POST':
        try:
            quantity = int(request.POST.get('quantity', 0))
            if quantity <= 0:
                messages.error(request, 'Ensure this value is greater than 0.')
                return render(request, 'orders/place_order.html', {'drug': drug})
            
            if quantity > drug.stock_quantity:
                messages.error(request, 'Insufficient stock available.')
                return render(request, 'orders/place_order.html', {'drug': drug})
            
            total_price = drug.price * quantity
            Order.objects.create(
                user=request.user,
                drug=drug,
                quantity=quantity,
                total_price=total_price
            )
            # Reduce the stock quantity of the drug
            drug.stock_quantity -= quantity
            drug.save()

            messages.success(request, 'Order placed successfully!')
            return redirect('orders:order_list')
        except ValueError:
            messages.error(request, 'Invalid quantity entered.')
            return render(request, 'orders/place_order.html', {'drug': drug})
    return render(request, 'orders/place_order.html', {'drug': drug})

def order_detail(request, pk):
    if not request.user.is_authenticated:  # Ensure the user is logged in
        messages.error(request, "You need to be logged in to view order details.")
        return redirect('users:login')
    order = get_object_or_404(Order, id=pk, user=request.user)
    return render(request, 'orders/order_detail.html', {'order': order})

def cancel_order(request, pk):
    if not request.user.is_authenticated:  # Ensure the user is logged in
        messages.error(request, "You need to be logged in to cancel an order.")
        return redirect('users:login')
    order = get_object_or_404(Order, id=pk, user=request.user)
    if request.method == 'POST':
        # Optional: Add logic to refund or restock items
        order.delete()
        messages.success(request, 'Order canceled successfully.')
        return redirect('orders:order_list')
    return render(request, 'orders/cancel_order.html', {'order': order})

