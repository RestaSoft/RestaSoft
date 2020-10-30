from django.db import models

# Create your models here.

class Staffs(models.Model):
    user_id=models.IntegerField()
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.IntegerField()
    store_id=models.IntegerField()
    permissions_id=models.IntegerField()


class Permission(models.Model):
    name_permission=models.CharField(max_length=50)

class Stores(models.Model):
    store_name=models.CharField(max_length=100)
    phone=models.IntegerField()
    email=models.EmailField()
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    zip_code=models.IntegerField()

class Products(models.Model):
    product_name=models.CharField(max_length=50)
    category_id=models.IntegerField()
    list_price=models.IntegerField()
    supplier_id=models.IntegerField()

class Orders(models.Model):
    staff_id=models.IntegerField()
    order_status=models.IntegerField()
    order_date=models.DateField()

class Order_items(models.Model):
    order_id=models.IntegerField()
    quantity=models.IntegerField()
    list_price=models.IntegerField()

class Suppliers(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.IntegerField()
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    zip_code=models.IntegerField()

class Categories_product(models.Model):
    category_description=models.CharField(max_length=100)
    category_name=models.CharField(max_length=50)

class Stocks(models.Model):
    product_id=models.IntegerField()
    quantity=models.IntegerField()
    store_id=models.IntegerField()
    
