from django.shortcuts import render,redirect
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework import filters, pagination
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.permissions import BasePermission
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse

# Create your views here.

class CartFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        customer_id = request.query_params.get('user_id')
        print(customer_id)
        if customer_id:
            return queryset.filter(Customer=customer_id)
        return queryset
    

class CartViewset(viewsets.ModelViewSet):
    queryset = models.Cart.objects.all()
    serializer_class = serializers.CartSerializer
    filter_backends= [CartFilterBackend]

@api_view(['DELETE'])
def remove_from_cart(request, cart_id):
    try:
        # Get the cart item to delete
        cart_item = get_object_or_404(models.Cart, id=cart_id)
        cart_item.delete()
        return JsonResponse({'message': 'Item removed from cart successfully'}, status=204)
    except models.Cart.DoesNotExist:
        return JsonResponse({'error': 'Cart item not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)



class BrandViewset(viewsets.ModelViewSet):
    queryset = models.Brand.objects.all()
    serializer_class = serializers.BrandSerializer

class CategoryViewset(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer

class SizeViewset(viewsets.ModelViewSet):
    queryset = models.Size.objects.all()
    serializer_class = serializers.SizeSerializer







class ProductViewset(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['brand__brand', 'category__category','product_name']
    ordering_fields = ['price']

    





class productFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        product_id = request.query_params.get('product')
        print(product_id)
        if product_id:
            return queryset.filter(product=product_id)
        return queryset

class ProductReviewerFilter(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        user_id = request.query_params.get('reviewer')
        print(user_id)
        if user_id:
            return queryset.filter(reviewer=user_id)
        return queryset

class ReviewViewset(viewsets.ModelViewSet):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer
    filter_backends = [productFilterBackend, ProductReviewerFilter]
    





