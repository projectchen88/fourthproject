from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from .forms import NewDish, EditDish
from accounts.views import index
from django.contrib.auth.decorators import login_required
from recipe.models import Dish

# Create your views here.
def admin_page(request):
    result = Dish.objects.all()
    return render(request, 'admin_page.html', {
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
        return redirect(admin_page)
    else:
        new_dish_form = NewDish()
        return render(request, 'new_dish.html',{
            'form'  :   new_dish_form
        })

@login_required
def edit_dish(request):
    edit_dish_form = EditDish()
    return render(request,'edit_dish.html',{
        'form'  :   edit_dish_form,
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
    return redirect(admin_page)   