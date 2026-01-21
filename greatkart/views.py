from django.shortcuts import render , get_object_or_404
from store.models import *
def home(request):
    products = Product.objects.all().filter(is_available=True)#لو متاح اعرض غير كده متعرصش
    context={
        'products':products,
    }
    return render(request , 'home.html' ,context)