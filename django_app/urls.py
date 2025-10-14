from django.urls import path
from . import views

urlpatterns = [
    path ( '', views.index, name='index' ),
    path ( 'categories/', views.categories, name='categories' ),
    path ( 'products/', views.products, name='products' ),
    path ( 'orders/', views.orders, name='orders' ),
    path ( 'order-details/', views.order_details, name='order_details' ),
    path ( 'categories_bootstrap/', views.categories_bootstrap, name='categories_bootstrap' ),
    path ( 'products_bootstrap/', views.product_bootstrap, name='products_bootstrap' ),
    path ( 'orders_bootstrap', views.orders_bootstrap, name='orders_bootstrap' ),
    path ( 'order_details_bootstrap', views.order_details_bootstrap, name='order_details_bootstrap' )
]