from django.contrib import admin
from app.models import Company,Product

# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
    list_display=['id','company_id','gst']


class ProductAdmin(admin.ModelAdmin):
    list_display=['id','company','product_name','product_price','quantity','total_price']
    # ordering = ['company','quantity']
    # search_fields =  ['product_name']

admin.site.register(Company,CompanyAdmin)
admin.site.register(Product,ProductAdmin)



    # list_filter = ('is_admin',)

    # fieldsets = (
    #     (None, {'fields': ('username', 'email','password')}),

    #     ('Permissions', {'fields': ('is_admin',)}),