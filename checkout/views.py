from django.shortcuts import render, get_object_or_404
from recipe.models import Dish

# Create your views here.
def checkout(request, id):
    result = get_object_or_404(Dish, pk=id)
    return render(request,'checkout.html',{
        'data' : result, 
    })
    
def paynow(request):
    return "paynow"