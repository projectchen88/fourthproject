from django.urls import path
from .views import index, logout, login

urlpatterns = [
    path('', index, name='index'),
    path('/logout', logout, name='logout'),
    path('login/', login, name='login'),
]