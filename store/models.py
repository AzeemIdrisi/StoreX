from django.db import models
from category.models import Category

# Create your models here.


class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    brand = models.CharField(max_length=200, null=True)
    model = models.CharField(max_length=200, blank=True, null=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(max_length=500, blank=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to="images/products")
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name


class VariantManager(models.Manager):
    def color(self):
        return super(VariantManager, self).filter(
            variation_category="Color", is_active=True
        )

    def size(self):
        return super(VariantManager, self).filter(
            variation_category="Size", is_active=True
        )


variation_category_choice = (
    ("Color", "Color"),
    ("Size", "Size"),
)


class Variant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variation_category = models.CharField(
        max_length=100, choices=variation_category_choice
    )
    variation_value = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now=True)
    objects = VariantManager()

    def __str__(self) -> str:
        return str(self.product.product_name + " : " + self.variation_value)
