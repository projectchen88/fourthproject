from django.urls import path
from recipe.views import show_dish

urlpatterns = [
    path('', show_dish, name='show_dish'),
]