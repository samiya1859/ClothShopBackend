from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()
router.register('brand', views.BrandViewset)
router.register('category', views.CategoryViewset)
router.register('sizes', views.SizeViewset)
router.register('reviews', views.ReviewViewset)
router.register('list', views.ProductViewset)
router.register('carts', views.CartViewset)

# Remove the custom action registration
# router.register('custom-cart-products', views.CartViewset, basename='custom_cart_products')

urlpatterns = [
    path('', include(router.urls)),
    path('cartremove/<int:cart_id>/', views.remove_from_cart, name='remove_from_cart'),
    # path('custom-cart-products/', views.GetCartProducts.as_view(), name='custom_cart_products'),
    # Add other URL patterns as needed
]
