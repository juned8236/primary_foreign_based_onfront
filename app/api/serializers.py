from app.models import Company,Product
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'
        

class CompanySerializer(serializers.ModelSerializer):
    Company_product=ProductSerializer(read_only=True,many=True)
    class Meta:
        model=Company
        fields = [
            'id',
            'company',
            'gst',
            "Company_product"
        ]
        

