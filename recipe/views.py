from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from .forms import NewDish
from accounts.views import index
# Create your views here.
def show_dish(request):
    if request.method == "POST":
        new_dish_entry = NewDish(request.POST, request.FILES)
        if new_dish_entry.is_valid():
            # instance = new_dish_entry.save(commit=False)
            # instance.user = request.user
            # instance.save()
            pass
        return redirect(index)


    new_dish_entry = NewDish()
    return render(request, 'new_dish.html'
    ,{
        'form' : new_dish_entry
        }
        )