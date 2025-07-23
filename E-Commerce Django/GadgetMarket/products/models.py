from tkinter.constants import CASCADE

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from categories.models import Categories
# Create your models here.

# name
# description
# category
# image
# price
# quantity
# status = 1
# is delete = 0
# created at ---> current
# updated at ----> current
# created by ----> admin
# updated by -----> admin

class Status(models.TextChoices):
    YES = '1', "YES"
    NO = '0', 'NO'


class Products(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    category = models.ForeignKey(Categories,on_delete=models.SET_NULL,null=True,related_name="category_name")
    image = models.TextField(null=True)
    price = models.IntegerField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=1,choices= Status.choices, default=Status.YES)
    is_delete = models.CharField(max_length=1,choices= Status.choices, default=Status.NO)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products_created')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products_updated')
