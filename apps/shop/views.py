from django.shortcuts import render
from matplotlib.style import context
from numpy import product

from apps.shoppingcart.models import Order
from .models import *
# Create your views here.
def store(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all() 
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items':0}

    context = {'items':items}

    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'store.html', context)

