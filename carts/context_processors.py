from .models import *
from django.db.models import Sum
from .views  import _cart_id
def counter(request):
    cart_count = 0
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_count = CartItem.objects.filter(cart=cart).aggregate(
            total=Sum('quantity')
        )['total'] or 0
    except Cart.DoesNotExist:
        pass
    return {'cart_count': cart_count}