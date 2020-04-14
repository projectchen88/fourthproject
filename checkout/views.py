from django.shortcuts import render, redirect, reverse, get_object_or_404
from recipe.models import Dish
from accounts.views import index
import stripe
from django.conf import settings

# Create your views here.
def checkout(request, id):
    result = get_object_or_404(Dish, pk=id)
    return render(request,'checkout.html',{
    'data' : result
    })
    # else:
        # return render(request, 'paynow.html')
    

# def paynow(request):
#     if request.method == 'GET':
#         amount = 1000 # or request.GET['amount']
#         key = settings.STRIPE_PUBLISHABLE_KEY #1
#         return render(request, 'donate/charge.html',{
#             'key' : key,
#             'amount' : amount
#         })
#     else:
#         stripe.api_key = settings.STRIPE_SECRET_KEY #2
#         charge = stripe.Charge.create(
#             amount= 1000,
#             currency='sgd',
#             description='Test charge',
#             source=request.POST['stripeToken']
#         )
#         return redirect(reverse('index'))

def paynow(request, id, dish_price):
    result = get_object_or_404(Dish, pk=id)

    if request.method == 'GET':
        key = settings.STRIPE_PUBLISHABLE_KEY #1
        amount = result.dish_price
        return render(request, 'paynow.html', {
            'key' : key,
            'amount' : dish_price
        })
    else:
        stripe.api_key = settings.STRIPE_SECRET_KEY #2
        charge = stripe.Charge.create(
            amount= dish_price,
            currency='sgd',
            description='Test charge',
            source=request.POST['stripeToken']
        )
        return redirect(reverse('index'))