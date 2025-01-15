from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Order
from drugs.models import Drug
from django.contrib.auth.decorators import login_required
from django.db import transaction
import logging
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import OrderSerializer
from rest_framework.views import APIView

# Create a logger object
logger = logging.getLogger(__name__)

# Set the logging level
logger.setLevel(logging.DEBUG)

# Create a console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# Create a formatter and add it to the handler
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(ch)

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
    """Cancel an order and update its status."""
    order = get_object_or_404(Order, id=pk, user=request.user)
    if request.method == 'POST':
        drug = order.drug
        logger.debug(f"Stock before cancel: {drug.stock_quantity}")
        if order.status != 'CANCELED':
            logger.debug(f"Cancelling order with ID {order.id} and drug {drug.name}")
            order.status = 'CANCELED'
            order.save()
            logger.debug(f"Order with ID {order.id} has been canceled, status updated to: {order.status}")
            messages.success(request, 'Order canceled successfully.')
        else:
            messages.warning(request, 'This order has already been canceled.')
        return redirect('orders:order_list')
    return render(request, 'orders/cancel_order.html', {'order': order})

@login_required
def order_detail(request, pk):
    """View to display details of a specific order."""
    order = get_object_or_404(Order, id=pk, user=request.user)
    return render(request, 'orders/order_detail.html', {'order': order})

@login_required
def order_history(request):
    """View to show order history of the logged-in user."""
    orders = Order.objects.filter(user=request.user)
    return render(request, 'orders/order_history.html', {'orders': orders})

# API views

class OrderViewSet(viewsets.ModelViewSet):
    """API view for managing orders."""
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Filter orders for the logged-in user."""
        return self.queryset.filter(user=self.request.user)

    @action(detail=True, methods=['post'])
    def cancel(self, request, pk=None):
        """API action to cancel an order."""
        order = self.get_object()
        if order.status != 'CANCELED':
            order.status = 'CANCELED'
            order.save()
            return Response({'status': 'Order canceled'}, status=status.HTTP_200_OK)
        else:
            return Response({'status': 'Order already canceled'}, status=status.HTTP_400_BAD_REQUEST)
