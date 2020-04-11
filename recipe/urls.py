from django.urls import path
from recipe.views import show_dish, new_dish,delete_dish

urlpatterns = [
    path('', show_dish, name='show_dish'),
    path('new_dish/', new_dish, name='new_dish'),
    path('delete_dish/<id>', delete_dish, name='delete_dish'),
]