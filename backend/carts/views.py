from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
def home(request):

    food_list = Product.objects.all()

    context = {
        'name': food_list.name,
        'price': food_list.price,
    }

    return render(request, 'base.html', context = context)