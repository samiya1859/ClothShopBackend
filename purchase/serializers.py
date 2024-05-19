from rest_framework import serializers
from . import models

class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PurchaseItem
        fields = '__all__'

class WishlistItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.WishlistItems
        fields= '__all__'
