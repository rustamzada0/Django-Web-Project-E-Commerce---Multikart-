from django.urls import path
from .views import *

app_name = 'payment'

urlpatterns=[
    path('checkout/', checkout , name='checkout'),
    path('order-success/',order_success, name='order-success')
]