from .models import Cart, CartItem
from django.db.models import Sum
from .views import _cart_id

def counter(request):
    cart_count = 0
    try:
        if request.user.is_authenticated:
            cart_count = CartItem.objects.filter(
                user=request.user
            ).aggregate(
                total=Sum('quantity')
            )['total'] or 0
        else:
            cart = Cart.objects.get(cart_id=_cart_id(request))
            cart_count = CartItem.objects.filter(
                cart=cart
            ).aggregate(
                total=Sum('quantity')
            )['total'] or 0

    except Cart.DoesNotExist:
        cart_count = 0

    return {'cart_count': cart_count}
