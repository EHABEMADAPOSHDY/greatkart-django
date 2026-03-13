from django.shortcuts import render
from store.models import *
def home(request):
    products = Product.objects.filter(
        is_available=True
    ).order_by('created_date')

    reviews = ReviewRating.objects.filter(status=True)

    context = {
        'products': products,
        'reviews': reviews,
    }

    return render(request, 'home.html', context)