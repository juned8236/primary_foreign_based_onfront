from django.db import models
# Create your models here.
class Company(models.Model):
    company = models.CharField(max_length = 255,unique=True) 
    gst = models.CharField(max_length = 255)

    class Meta:
        ordering = ('id','company','gst')
    def __str__(self):
        return self.company

class Product(models.Model):
    #below company db used in serializer.py to display both thing in api
    product_name = models.CharField(max_length = 255,unique=True,null=True, blank=True)
    product_price = models.FloatField(null=True, blank=True)
    quantity = models.IntegerField(default=1)
    total_price = models.FloatField(null=True, blank=True)
    company=models.ForeignKey(Company,on_delete=models.CASCADE,related_name="Company_product")

    def __str__(self):
        return self.product_name



    # for adding multiple primary_key 
    # class Meta:
    #     unique_together = (("product_name", "id"))
