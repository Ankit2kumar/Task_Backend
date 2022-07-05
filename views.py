from django.http import JsonResponse
from django.shortcuts import render
from .models import Product,SubProduct,Category,MainTable

def general_details(request):
    products = list(Product.objects.all().values_list('product_name',flat=True))
    categories = list(Category.objects.all().values_list('category_name',flat=True))
    subproducts = list(SubProduct.objects.all().values_list('sub_name',flat=True))

    result = {
        'products': products,
        'categories': categories,
        'subproducts': subproducts,
    }

    return JsonResponse(result)

def add_subproduct(request):
    name = request.POST.get('name')
    result = {}
    if name:
        SubProduct.objects.create(sub_name=name)

        subproducts = list(SubProduct.objects.all().values_list('sub_name',flat=True))
        result = {
            'status':'You have successfully created sub product',
            'subproducts': subproducts,
            'code':200
        }
    else:
        result = {'status':'Something went wrong'}
    return JsonResponse(result)


def save_details(request):
    products = request.POST.get('products')
    categories = request.POST.get('categories')
    subproducts = request.POST.get('subproducts')
    result = {}

    print(products,categories,subproducts)
    if products and categories and subproducts:
        MainTable.objects.create(product=products,subcategories=categories,subproducts=subproducts)

        result = {
            'status':'You have successfully saved details',
        }
    else:
        result = {'status':'Something went wrong'}
    return JsonResponse(result)