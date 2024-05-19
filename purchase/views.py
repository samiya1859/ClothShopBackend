from django.shortcuts import render,redirect
from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework import filters, pagination
from rest_framework.permissions import IsAuthenticated

from rest_framework.pagination import PageNumberPagination

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 6  # Number of items to include per page
    page_size_query_param = 'page_size'
    max_page_size = 1000

class ProductFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        customer_id = request.query_params.get('user_id')
        print(customer_id)
        if customer_id:
            return queryset.filter(customer=customer_id)
        return queryset

class PurchaseViewset(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = models.PurchaseItem.objects.all()
    serializer_class = serializers.PurchaseSerializer
    filter_backends = [ProductFilterBackend]
    pagination_class = StandardResultsSetPagination

    def perform_create(self, serializer):
        instance = serializer.save()
        # Decrease product quantity by 1
        product = instance.product
        product.quantity = max(0, product.quantity - 1)  # Ensure quantity doesn't go negative
        product.save()



    
class wishlistFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        customer_id = request.query_params.get('user_id')
        print(customer_id)
        if customer_id:
            return queryset.filter(customer=customer_id)
        return queryset

class WishlistViewset(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = models.WishlistItems.objects.all()
    serializer_class = serializers.WishlistItemSerializer
    filter_backends = [wishlistFilterBackend]
    pagination_class = StandardResultsSetPagination
