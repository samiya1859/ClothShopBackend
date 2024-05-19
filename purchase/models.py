from django.db import models
from django.contrib.auth.models import User
from products.models import Product

class PurchaseItem(models.Model):
    customer = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    purchase_time = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"{self.product.product_name+' : '+self.customer.first_name}"

class WishlistItems(models.Model):
    customer = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)

    def _str_(self):
        return f"{self.product.product_name+' : '+self.customer.user.first_name}"