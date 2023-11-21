from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category
from cart.models import CartItem
from cart.views import _cart_id
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q


# Create your views here.
def store(request):
    products = Product.objects.all().filter(is_available=True).order_by("id")
    items_count = products.count()
    print(items_count)
    # Handling the paginator for 3 products at 1 page
    paginator = Paginator(products, 3)
    page = request.GET.get("page")
    paged_products = paginator.get_page(page)

    context = {
        "items_count": items_count,
        "products": paged_products,  # before 'paged_products' it was 'products'
    }
    return render(request, "store/store.html", context)


def by_category(request, category_slug):
    categories = get_object_or_404(Category, slug=category_slug)
    products = (
        Product.objects.all()
        .filter(is_available=True, category=categories)
        .order_by("id")
    )

    # Handling the paginator for 3 products at 1 page
    paginator = Paginator(products, 3)
    page = request.GET.get("page")
    paged_products = paginator.get_page(page)
    items_count = products.count()
    context = {
        "items_count": items_count,
        "products": paged_products,
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


def search(request):
    keyword = request.GET["keyword"]
    if keyword:
        products = Product.objects.order_by("-created_date").filter(
            Q(description__icontains=keyword) | Q(product_name__icontains=keyword)
        )  # OR Operation for both conditions for title and description

    items_count = products.count()
    context = {
        "products": products,
        "items_count": items_count,
    }
    return render(request, "store/store.html", context)
