from django import forms
from .models import Dish

class NewDish(forms.ModelForm):
    class Meta:
        model = Dish        
        fields = ('dish_name','dish_info','dish_store','dish_price', 'dish_image')
        
class EditDish(forms.ModelForm):
    class Meta:
        model = Dish        
        fields = ('dish_name','dish_info','dish_store','dish_price', 'dish_image')        