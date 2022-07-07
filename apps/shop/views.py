from django.shortcuts import render
from matplotlib.style import context
from numpy import product
from .models import *
# Create your views here.
def store(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'store.html', context)

