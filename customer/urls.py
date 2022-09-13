from django.urls import path
from . import views

urlpatterns=[
    path('home',views.customer_home,name='home'),
    path('password',views.change_password,name='password'),
    path('order',views.my_order,name='order'),
    path('product',views.product_details,name='product'),
    path('profile',views.profile,name='profile'),
    path('cart',views.view_cart,name='cart'),
    path('master',views.master,name='master'),
    path('details',views.details,name='details'),
]
