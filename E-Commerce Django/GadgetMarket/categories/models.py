from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Status(models.TextChoices):
    YES = '1', "YES"
    NO = '0', 'NO'


class Categories(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    image = models.TextField(null=True)
    status = models.CharField(max_length=1,choices= Status.choices, default=Status.YES)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='categories_created')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='categories_updated')
