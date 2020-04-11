from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from .forms import NewDish
from accounts.views import index
from django.contrib.auth.decorators import login_required
from recipe.models import Dish

# Create your views here.
def show_dish(request):
    result = Dish.objects.all()
    return render(request, 'show_dish.html', {
       'data':result,
    })

@login_required
def new_dish(request):
    if request.method == "POST":
        new_dish_entry = NewDish(request.POST, request.FILES)
        if new_dish_entry.is_valid():
            instance = new_dish_entry.save(commit=False)
            instance.user = request.user
            instance.save()
            pass
        return redirect(show_dish)


    new_dish_entry = NewDish()
    return render(request, 'new_dish.html',{
        'form' : new_dish_entry
    })
    
@login_required
def confirm_delete_dish(request, id):
    result = get_object_or_404(Dish, pk=id)
    return render(request, "delete_dish.html", {
        'data' : result
    })

@login_required
def delete_dish(request, id):
    Dish.objects.filter(pk=id).delete()
    return redirect(show_dish)   