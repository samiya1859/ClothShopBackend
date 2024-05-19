from django.db import models
from django.contrib.auth.models import User
# from customer.models import Customers
from rest_framework.permissions import IsAuthenticated

SIZES = [
    ('S', 'S'),
    ('M', 'M'),
    ('L', 'L'),
    ('XL', 'XL'),
    ('XXL', 'XXL'),
    ('XXXL', 'XXXL'),
]

STAR_CHOICES = [
    ('⭐', '⭐'),
    ('⭐⭐', '⭐⭐'),
    ('⭐⭐⭐', '⭐⭐⭐'),
    ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'),
]

class Category(models.Model):
    category = models.CharField(max_length=50)
    slug = models.SlugField()

    def __str__(self):
        return self.category

class Brand(models.Model):
    brand = models.CharField(max_length=50)
    slug = models.SlugField()

    def __str__(self):
        return self.brand

class Size(models.Model):
    name = models.CharField(choices=SIZES, max_length=10)

    def __str__(self):
        return self.name

class Product(models.Model):
    product_name = models.CharField(max_length=50)
    category = models.ManyToManyField(Category)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, blank=True)
    color = models.CharField(max_length=20)
    image = models.ImageField(upload_to='products/images/')
    product_description = models.TextField(null=True,blank=True)
    quantity = models.IntegerField(default=0)
    sizes = models.ManyToManyField(Size)  # Change here
    availability_status = models.BooleanField(default=True)
    price = models.IntegerField(default=0)
    rating = models.CharField(choices=STAR_CHOICES,max_length=20,null=True,blank=True)
    

    

    def __str__(self):
        return self.product_name  


    


class Cart(models.Model):
    Customer = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    cancel = models.BooleanField(default=False,null=True,blank=True)

    def __str__(self) -> str:
        return f"{self.Customer.first_name +' : '+self.product.product_name}"


    
class Review(models.Model):
    reviewer = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    review = models.TextField()
    rating = models.CharField(choices=STAR_CHOICES,max_length=10)

    def __str__(self):
        return f"{self.reviewer.username} : {self.product.product_name}"
        
