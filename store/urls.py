from django.urls import path
from . import views


urlpatterns = [
    # /store/ root
    path("", views.store, name="store"),
    path("category/<slug:category_slug>/", views.by_category, name="by_category"),
    path(
        "category/<slug:category_slug>/<slug:product_slug>/",
        views.product_detail,
        name="product_detail",
    ),
    path(
        "search/",
        views.search,
        name="search",
    ),
]
