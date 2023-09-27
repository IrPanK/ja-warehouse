from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
    price = models.IntegerField()
    category = models.CharField(max_length=255)
    add_date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
