from django.urls import path
from checkout.views import paynow

urlpatterns = [
    path('paynow/<id>/', paynow, name='paynow'),
]