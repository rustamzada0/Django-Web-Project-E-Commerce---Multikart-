from django.db import models
from django.db.models.fields import CharField, TextField, FloatField, BooleanField
from django.db.models.fields.files import ImageField
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import AbstractUser
from core.models import AbstractModel
from django.contrib.auth.models import User
from django.utils.text import slugify
from core.models import *
from product.models import *

# Create your models here.


class User(AbstractUser):
    first_name = CharField(max_length=50, null=True, blank=True, default='')
    last_name = CharField(max_length=50, null=True, blank=True, default='')
    password = CharField(max_length=255, null=True, blank=True, default='')
    email = CharField(max_length=50, null=True, blank=True, default='')
    phone_number = CharField(max_length=50, null=True, blank=True, default='')
    flat = CharField(max_length=50, null=True, blank=True, default='')
    address = CharField(max_length=100, null=True, blank=True, default='')
    zip_code = CharField(max_length=50, null=True, blank=True, default='')
    country = CharField(max_length=50, null=True, blank=True, default='')
    city = CharField(max_length=50, null=True, blank=True, default='')
    region = CharField(max_length=50, null=True, blank=True, default='')
    card = CharField(max_length=16, null=True, blank=True, default='')
    forget_pwd_token = CharField(max_length=100,null=True,blank=True)
    email_confirmed = BooleanField(default=False)


class WishList(AbstractModel):
    user = ForeignKey(User, on_delete=models.CASCADE)
    variant = ForeignKey("product.Variant", on_delete=models.CASCADE)

    def title(self):
        return self.variant.title
    
    def username(self):
        return self.user.get_full_name()
    
    def user_id(self):
        return self.user.id
    
    def product_photo(self):
        image = Image.objects.filter(variant = self.variant).filter(is_main=True).first()
        if image:
            return mark_safe('<img src="{}" width="100"/>'.format(image.image.url))


class Cart(AbstractModel):
    user = ForeignKey(User, on_delete=models.CASCADE)
    product = ForeignKey("product.Product", on_delete=models.CASCADE)


class Review(AbstractModel):
    user = ForeignKey(User, on_delete=models.CASCADE)
    variant = ForeignKey("product.Variant", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    text = models.TextField()
    rating = models.IntegerField(null=True, blank=True)

    def get_title(self):
        return self.variant.title
    
    def username(self):
        return self.user.get_full_name()
    
    def user_id(self):
        return self.user.id
    
    def product_photo(self):
        image = Image.objects.filter(variant = self.variant).filter(is_main=True).first()
        if image:
            return mark_safe('<img src="{}" width="100"/>'.format(image.image.url))