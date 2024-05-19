from rest_framework.routers import DefaultRouter
from django.urls import path,include
from . import views

router = DefaultRouter()
router.register('buy',views.PurchaseViewset)
router.register('wishlist',views.WishlistViewset)

urlpatterns = [
    path('',include(router.urls)),
]
