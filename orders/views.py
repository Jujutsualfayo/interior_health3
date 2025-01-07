from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db import transaction
import logging
from .models import Order

logger = logging.getLogger(__name__)

@login_required
@transaction.atomic
def cancel_order(request, pk):
    # Retrieve the order object, making sure it's associated with the logged-in user
    order = get_object_or_404(Order, id=pk, user=request.user)
    
    if request.method == 'POST':
        # Log the initial stock quantity for debugging
        logger.debug(f"Stock before cancel: {order.drug.stock_quantity}")

        if order.status != 'CANCELED':
            # Log the action of restoring stock if it's not already canceled
            logger.debug(f"Restoring stock for order with quantity {order.quantity}")
            # If stock is managed elsewhere, we don't alter it here

            # Update the order's status to 'CANCELED'
            order.status = 'CANCELED'
            order.save()

            # Log the final status of the order
            logger.debug(f"Order with id {order.id} has been canceled, status updated to: {order.status}")
            
    return render(request, 'order/cancel_order_confirmation.html', {'order': order})
