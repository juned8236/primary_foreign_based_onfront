from django.contrib import admin
from app.models import Company,Product

# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
    list_display=['company_id','gst']

class ProductAdmin(admin.ModelAdmin):
    list_display=['company','product_name','product_price','quantity','total_price']

admin.site.register(Company,CompanyAdmin)
admin.site.register(Product,ProductAdmin)

