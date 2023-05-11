from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.utils.translation import gettext_lazy as _



class Region(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=50)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}|{self.region.name}'


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product(models.Model):
    sale_rent = (
        (1, 'For Sale'),
        (2, 'For Rent')
    )

    address = models.CharField(max_length=150)
    price = models.FloatField()
    image1 = models.ImageField(upload_to='pics')
    image2 = models.ImageField(upload_to='pics')
    image3 = models.ImageField(upload_to='pics', blank=True, null=True)
    image4 = models.ImageField(upload_to='pics', blank=True, null=True)
    image5 = models.ImageField(upload_to='pics', blank=True, null=True)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, blank=True, null=True)
    description = models.TextField()
    sale_rent = models.IntegerField(choices=sale_rent)

    def __str__(self):
        return self.address


class ProductInfo(models.Model):
    room_count = models.IntegerField(default=1)
    bath_room = models.IntegerField(default=1)
    has_garage = models.BooleanField(default=False)
    square = models.FloatField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.address


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    message = models.TextField()

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


class UserProductView(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.address


class Message(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.subject

# class User(AbstractUser):
#     class Status(models.TextChoices):
#         ADMIN = 'admin', 'Admin'
#         CLIENT = 'client', 'Client'
#         VIP_CLIENT = 'vip_client', 'Vip client'
#
#     status = models.CharField(max_length=50, choices=Status.choices, default=Status.CLIENT)
#     email = models.EmailField(unique=True)
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(args, kwargs)
#         self.cart_set = None
#
#     @property
#     def cart_count(self):
#         cart = self.cart_set.filter(is_active=True).first()
#         if cart:
#             return cart.cartitem_set.count()
#         return 0
#
# class Tag(models.Model):
#     name = models.CharField(max_length=255)
#
#     def __str__(self):
#         return self.name
#
#
# class BaseModel:
#     pass
#
#
# class Product(BaseModel):
#     title = models.CharField(max_length=255)
#     price = models.IntegerField()
#     short_description = models.TextField()
#     description = models.TextField(blank=True, null=True)
#     discount = models.IntegerField(null=True, blank=True)
#     quantity = models.IntegerField()
#     is_premium = models.BooleanField(default=False)
#     shopping_cost = models.SmallIntegerField(default=0)
#     tags = models.ForeignKey('app.Tag', models.CASCADE, blank=True, default=1)
#     category = models.ForeignKey('app.Category', models.CASCADE)
#     specification = models.JSONField(default=dict, blank=True)
#     author = models.ForeignKey('app.User', models.CASCADE)
#
#     def __str__(self):
#         return self.title
#
#     @property
#     def discount_price(self):
#         return self.price - self.price * self.discount // 100

