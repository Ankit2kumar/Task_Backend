from django.db import models


class SubProduct(models.Model):
    sub_name = models.CharField(max_length=200,default='')

class Category(models.Model):
    category_name = models.CharField(max_length=200,default='')
    
class Product(models.Model):
    product_name = models.CharField(max_length=200,default='')

class MainTable(models.Model):
    product = models.CharField(max_length=200,default='')
    subcategories = models.CharField(max_length=500,default='')
    subproducts = models.CharField(max_length=500,default='')

   
    

