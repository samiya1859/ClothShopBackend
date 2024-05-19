from rest_framework import serializers
from .models import Brand,Category,Product,Size,Cart,STAR_CHOICES,Review



class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ['name']        

class ProductSerializer(serializers.ModelSerializer):
    # product_name = serializers.StringRelatedField(many=False)
    brand = serializers.StringRelatedField(many=False)
    category = serializers.StringRelatedField(many=True)
    sizes = serializers.StringRelatedField(many=True)
    quantity = serializers.IntegerField()

    class Meta:
        model = Product
        fields = '__all__'




class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['Customer','product','quantity']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'