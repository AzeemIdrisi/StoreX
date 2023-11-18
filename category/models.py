from django.db import models
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(null=False, unique=True)
    description = models.TextField(max_length=255, blank=True)
    category_image = models.ImageField(upload_to="images/categories", blank=True)

    def __str__(self) -> str:
        return self.category_name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def get_url(self):
        return reverse("by_category", args=[self.slug])
