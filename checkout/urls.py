from django.urls import path
from checkout.views import checkout, paynow

urlpatterns = [
    path('<id>/', checkout, name='checkout'),
    path('<id>/paynow/<dish_price>/', paynow, name='paynow'),
]