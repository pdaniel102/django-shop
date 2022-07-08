from .models import Order, OrderItem

def total_cart_items(request):
    
    if request.user.is_authenticated:
        customer = request.user.customer

        order = Order.objects.get(customer=customer, complete=False)

        if order:
            orderitems = OrderItem.objects.filter(order=order)
            qty = sum([item.quantity for item in orderitems])

        else:
            qty = 0

    else:
        qty = 0
        items = []
        order = {'get_cart_total': 0, 'get_cart_items':0}
        qty = order['get_cart_items']

    return {'qty': qty}