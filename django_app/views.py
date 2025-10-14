from django.shortcuts import render
from .models import *


def index(request) :
    categories = Category.objects.all ()
    products = Product.objects.all ()
    orders = Order.objects.all ()
    order_details = OrderDetails.objects.all ()
    context = {
        'categories' : categories,
        'products' : products,
        'orders' : orders,
        'order_details' : order_details
    }
    return render ( request, 'index.html', context )


def categories(request) :
    categories = Category.objects.all ()
    return render ( request, 'categories.html', {'categories' : categories} )


def products(request) :
    products = Product.objects.all ()
    return render ( request, 'products.html', {'products' : products} )


def orders(request) :
    orders = Order.objects.all ()
    return render ( request, 'orders.html', {'orders' : orders} )


def order_details(request) :
    order_details = OrderDetails.objects.all ()
    return render ( request, 'order_details.html', {'order_details' : order_details} )


def categories_bootstrap(request) :
    categories = Category.objects.all ()
    return render ( request, 'categories_bootstrap.html', {'categories' : categories} )


def product_bootstrap(request):
    products = Product.objects.all ()
    return render ( request, 'products_bootstrap.html', { 'products': products } )


def orders_bootstrap(request) :
    orders = Order.objects.all ()
    return render ( request, 'orders_bootstrap.html', {'orders' : orders} )


def order_details_bootstrap(request) :
    order_details = OrderDetails.objects.all ()
    return render ( request, 'order_details_bootstrap.html', {'order_details' : order_details} )