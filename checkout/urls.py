from django.urls import path
from checkout.views import checkout, paynow

urlpatterns = [
    path('<id>/', checkout, name='checkout'),
    path('paynow/', paynow, name='paynow'),
]