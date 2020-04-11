from django.urls import path
from recipe.views import admin_page, new_dish, edit_dish, confirm_delete_dish, delete_dish

urlpatterns = [
    path('', admin_page, name='admin_page'),
    path('new_dish/', new_dish, name='new_dish'),
    path('edit_dish/', edit_dish, name='edit_dish'),
    path('confirm_delete_dish/<id>', confirm_delete_dish, name='confirm_delete_dish'),
    path('delete_dish/<id>', delete_dish, name='delete_dish'),
]