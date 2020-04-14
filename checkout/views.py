from django.shortcuts import render, redirect, reverse, get_object_or_404
from recipe.models import Dish
from accounts.views import index
import stripe
from django.conf import settings

# Create your views here.
def paynow(request, id):
    result = get_object_or_404(Dish, pk=id)
    amount = int(result.dish_price * 100)

    if request.method == 'GET':
        key = settings.STRIPE_PUBLISHABLE_KEY #1
        return render(request, 'paynow.html', {
            'key' : key,
            'amount' : amount,
            'data' : result,
        })
    else:
        stripe.api_key = settings.STRIPE_SECRET_KEY #2
        charge = stripe.Charge.create(
            amount= amount,
            currency='sgd',
            description='2nd charge',
            source=request.POST['stripeToken']
        )
        return redirect(reverse('index'))