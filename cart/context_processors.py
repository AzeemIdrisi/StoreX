from .models import Cart, CartItem
from .views import _cart_id


def counter(request):
    cart_count = 0
    try:
        cart = Cart.objects.filter(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart[:1])

        for item in cart_items:
            cart_count += item.quantity
    except Cart.DoesNotExist:
        pass
    return dict(cart_count=cart_count)
