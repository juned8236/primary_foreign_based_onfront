from django.db import models

# Create your models here.
class Company(models.Model):
    company_id = models.CharField(max_length = 255,unique=True,null=True, blank=True) 
    gst = models.CharField(max_length = 255)
    def __str__(self):
        return self.company_id

class Product(models.Model):
    product_name = models.CharField(max_length = 255,unique=True,null=True, blank=True)
    company=models.ForeignKey(Company,on_delete=models.CASCADE,null=True, blank=True)
    product_price = models.FloatField(null=True, blank=True)
    quantity = models.IntegerField(default=1)
    total_price = models.FloatField(null=True, blank=True)
    def __str__(self):
        return self.product_name



    # for adding multiple primary_key 
    # class Meta:
    #     unique_together = (("product_name", "id"))
