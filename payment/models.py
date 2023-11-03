from django.db import models
from django.db.models.fields import CharField, TextField, IntegerField, EmailField, BooleanField
from core.models import AbstractModel

# Create your models here.

class Billing(AbstractModel):
    first_name = CharField()
    last_name = CharField()
    email = EmailField()
    phone_number = CharField()
    flat = CharField()
    address = TextField()
    zip_code = IntegerField()
    country = CharField()
    city = CharField()
    region = CharField()
    shipping = BooleanField(null=False)
    payment = CharField(null=False)

# dffddfsdfs