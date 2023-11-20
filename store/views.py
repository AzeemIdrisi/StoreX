from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category
from cart.models import CartItem
from cart.views import _cart_id


# Create your views here.
def store(request):
    products = Product.objects.all().filter(is_available=True)
    context = {
        "products": products,
    }
    return render(request, "store/store.html", context)


def by_category(request, category_slug):
    categories = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.all().filter(is_available=True, category=categories)
    context = {
        "products": products,
    }
    return render(request, "store/store.html", context)


def product_detail(request, category_slug, product_slug):
    product = get_object_or_404(
        Product,
        category__slug=category_slug,  # Double underscore is used to access nested attribute
        slug=product_slug,
    )
    in_cart = CartItem.objects.filter(
        cart__cart_id=_cart_id(request), product=product
    ).exists()
    return render(
        request,
        "store/product_detail.html",
        {
            "product": product,
            "in_cart": in_cart,
        },
    )
