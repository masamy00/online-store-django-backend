from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(ProductPhoto)
admin.site.register(ProductTag)
admin.site.register(ProductReview)
admin.site.register(SizeCategory)
admin.site.register(Size)
admin.site.register(ColorCategory)
admin.site.register(Color)
admin.site.register(ProductStock)
