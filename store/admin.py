from django.contrib import admin
from .models import Product, Variant

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "product_name",
        "price",
        "stock",
        "category",
        "modified_date",
        "is_available",
    )
    prepopulated_fields = {
        "slug": ("product_name",),
    }


class VariantAdmin(admin.ModelAdmin):
    list_display = (
        "product",
        "variation_category",
        "is_active",
    )
    list_editable = ("is_active",)
    list_filter = (
        "product",
        "variation_category",
        "variation_value",
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Variant, VariantAdmin)
