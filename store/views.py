from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category


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
