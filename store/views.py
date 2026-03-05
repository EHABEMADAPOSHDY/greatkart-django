from django.shortcuts import render , redirect , get_object_or_404
from django.http import HttpResponse
from .models import *
from carts.models import *
from carts.views import _cart_id
from django.contrib import messages 
from django.core.paginator import EmptyPage , PageNotAnInteger , Paginator
from django.db.models import Q
from .forms import *
from orders.models import *

def store(request , category_slug=None):
    categories = None
    products = None
    if category_slug != None:
        categories=get_object_or_404(Category , slug=category_slug)
        products=Product.objects.filter(category=categories , is_available=True)
        paginator = Paginator(products , 1)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        products_count = products.count()
    else:
        products  = Product.objects.select_related('category').filter(is_available=True).order_by('id')
        paginator = Paginator(products , 3)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        products_count= Product.objects.count()
    content = {
        'products' :paged_products , 
        'products_count' : products_count , 
    }
    return render(request , 'store/store.html' , content)

def product_detail(request, category_slug, product_slug):
    single_product = Product.objects.get(
        category__slug=category_slug,
        slug=product_slug
    )

    in_cart = CartItem.objects.filter(
        cart__cart_id=_cart_id(request),
        product=single_product
    ).exists()

    if request.user.is_authenticated:
        orderproduct = OrderProduct.objects.filter(
            user=request.user,
            product=single_product
        ).exists()
    else:
        orderproduct = False

    review = ReviewRating.objects.filter(
        product=single_product,
        status=True
    )

    context = {
        'single_product': single_product,
        'in_cart': in_cart,
        'orderproduct': orderproduct,
        'review': review,
    }

    return render(request, 'store/product_detail.html', context)

def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.order_by('-created_date').filter(Q(description__icontains=keyword)|Q(product_name__icontains=keyword))
            products_count = products.count()
    context = {
        'products':products,
        'products_count':products_count,
    }
    return render(request , 'store/store.html' , context)

def submit_review(request , product_id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        try:
            reviews = ReviewRating.objects.get(user__id=request.user.id , product_id = product_id)
            form = ReviewForm(request.POST , instance=reviews)
            form.save()
            messages.success(request , 'Thank you! Your review has been updated.')
            return redirect(url)
        except ReviewRating.DoesNotExist:
            form = ReviewForm(request.POST)
            if form.is_valid():
                data = ReviewRating()
                data.subject = form.cleaned_data['subject']
                data.rating = form.cleaned_data['rating']
                data.review = form.cleaned_data['review']
                data.ip = request.META.get('REMOTE_ADDR')
                data.product_id = product_id
                data.user_id = request.user.id
                data.save()
                messages.success(request , 'Thank you! Your review has been submitted.')
                return redirect(url)