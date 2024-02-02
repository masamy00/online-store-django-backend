from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models

from merchants.models import Merchant


# Create your models here.
class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_en_name = models.CharField(max_length=255, null=False, blank=False)
    category_ar_name = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.category_en_name


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, null=False, blank=False)
    merchant_id = models.ForeignKey(Merchant, on_delete=models.CASCADE, null=False, blank=False)
    product_en_name = models.CharField(max_length=255, null=False, blank=False)
    product_ar_name = models.CharField(max_length=255, null=False, blank=False)
    product_en_description = models.CharField(max_length=1000, null=False, blank=False)
    product_ar_description = models.CharField(max_length=1000, null=False, blank=False)
    has_sizes = models.BooleanField(default=False, null=False, blank=False)
    has_colors = models.BooleanField(default=False, null=False, blank=False)

    def __str__(self):
        return self.product_en_name


class ProductPhoto(models.Model):
    product_photo_id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, null=False, blank=False)
    photo = models.ImageField(upload_to='product_photos/')


class ProductTag(models.Model):
    product_tag_id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, null=False, blank=False)
    tag_name = models.CharField(max_length=50, null=False, blank=False)


class ProductReview(models.Model):
    product_review_id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, null=False, blank=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    rating = models.IntegerField(null=False, blank=False, validators=[
        MinValueValidator(0, message="Value must be greater than or equal to 0."),
        MaxValueValidator(5, message="Value must be less than or equal to 5.")
    ])
    review_text = models.TextField(max_length=1000, null=False, blank=False)
    date_posted = models.DateTimeField(default=timezone.now, blank=False, null=False)


class SizeCategory(models.Model):
    size_category_id = models.AutoField(primary_key=True)
    size_category_en_name = models.CharField(max_length=255, blank=False, null=False)
    size_category_ar_name = models.CharField(max_length=255, blank=False, null=False)


class Size(models.Model):
    size_id = models.AutoField(primary_key=True)
    size_category_id = models.ForeignKey(SizeCategory, on_delete=models.CASCADE, null=False)
    size_name = models.CharField(max_length=100, blank=False, null=False)


class ColorCategory(models.Model):
    color_category_id = models.AutoField(primary_key=True)
    color_category_en_name = models.CharField(max_length=255, blank=False, null=False)
    color_category_ar_name = models.CharField(max_length=255, blank=False, null=False)
    color_category_hex = models.CharField(max_length=100, blank=False, null=False)


class Color(models.Model):
    color_id = models.AutoField(primary_key=True)
    color_category_id = models.ForeignKey(ColorCategory, on_delete=models.CASCADE)
    color_name = models.CharField(max_length=255, blank=False, null=False)
    color_hex = models.CharField(max_length=50, blank=False, null=False)
    color_order = models.IntegerField(default=0, null=False, blank=False)


class ProductStock(models.Model):
    product_stock_id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, null=False, blank=False)
    size_id = models.ForeignKey(Size, on_delete=models.CASCADE, null=True, blank=True)
    color_id = models.ForeignKey(Color, on_delete=models.CASCADE, null=True, blank=True)
    qty = models.IntegerField(default=0, blank=False, null=False,
                              validators=[MinValueValidator(0, message="Value must be greater than or equal to 0.")])
