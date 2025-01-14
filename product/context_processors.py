from .models import Cart

def cart_context(request):
    cart_items = []
    cart_total = 0
    total_price = 0

    if request.user.is_authenticated:
        cart_items = Cart.objects.filter(user=request.user)
        cart_total = sum(item.quantity for item in cart_items)
        total_price = sum(item.product.price * item.quantity for item in cart_items)

    return {
        'cart_items': cart_items,
        'cart_total': cart_total,
        'total_price': total_price
    }
