from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from app import models
from django.http import HttpResponseRedirect, HttpResponse
from app.forms import CompanyForm

@csrf_exempt
def company_view(request):
    if request.method == 'POST':
        company_name = request.POST.get('company_name')
        gst = request.POST.get('gst')
        models.Company.objects.create(company_id=company_name,gst=gst)
        response=JsonResponse({'status':'Company Added sucessfully'})
        return response

    else:
        return render(request, 'company.html', {})

def add_product(request):
    data=models.Company.objects.all()
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        cost = request.POST.get('cost')
        comp1=request.POST.get('comp1')
        print(comp1)
        print(cost)
        print(product_name)
         
        #  1(a.)
        # a=models.Company.objects.get(company_id=comp1)
        # r=models.Product.objects.get_or_create(product_name=product_name,product_price=cost,product_id=a)   

        # or 2.b
        models.Product.objects.get_or_create(product_name=product_name,product_price=cost,company=data.get(company_id=comp1))           
        response=JsonResponse({'status':'Product Added sucessfully'})
        return response

    else:
        return render(request, 'get_product.html', {'data':data})
    return render(request,'get_product.html',{'data':data})
