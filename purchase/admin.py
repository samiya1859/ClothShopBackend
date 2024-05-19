from django.contrib import admin
from . import models
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
# Register your models here.

class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['customer_name','product_name','purchase_time']

    def customer_name(self,obj):
        return obj.customer.user.first_name
    def product_name(self,obj):
        return obj.product.product_name
    
    

admin.site.register(models.PurchaseItem,PurchaseAdmin)
