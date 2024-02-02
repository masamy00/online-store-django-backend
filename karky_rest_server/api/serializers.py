from rest_framework import serializers
from products.models import Product, ProductPhoto


class ProductPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPhoto
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    photos = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_photos(self, obj):
        photos = ProductPhoto.objects.filter(product_id=obj.product_id)
        serializer = ProductPhotoSerializer(photos, many=True)
        return serializer.data
