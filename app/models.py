from django.db import models

# Create your models here.
from django.contrib.auth.models import User,Group
class Company(models.Model):
    company_id = models.CharField(max_length = 255,primary_key=True) 
    gst = models.CharField(max_length = 255)

class Product(models.Model):
    product_id=models.ForeignKey(Company,on_delete=models.CASCADE)
    product_name = models.CharField(max_length = 255,primary_key=True)
    product_price = models.FloatField(null=True, blank=True)
    quantity = models.IntegerField(default=1)
    total_price = models.FloatField(null=True, blank=True)
