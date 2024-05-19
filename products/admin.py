from django.contrib import admin
from .models import Category,Brand,Product,Size,Cart,Review
# Register your models here.

class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('brand',),}

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category',),}



admin.site.register(Category,CategoryAdmin)
admin.site.register(Brand,BrandAdmin)
admin.site.register(Product)
admin.site.register(Review)
admin.site.register(Size)
admin.site.register(Cart)
# admin.site.register(WishlistItems)

