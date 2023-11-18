from django.urls import path
from . import views


urlpatterns = [
    # /store/ root
    path("", views.store, name="store"),
    path("<slug:category_slug>/", views.by_category, name="by_category"),
]
