from django.db import models

# Create your models here.

class Staffs(models.Model):
    staff_id=models.IntegerField()
    user_id=models.IntegerField()
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.IntegerField()
    store_id=models.IntegerField()
    permissions=models.IntegerField()


class Permission(models.Model):
    permission_id=models.IntegerField()
    name_permission=models.CharField(max_length=50)

class Stores(models.Model):
    stores_id=models.IntegerField()
    store_name=models.CharField(max_length=100)
    phone=models.IntegerField()
    email=models.EmailField()
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    zip_code=models.IntegerField()

class Products(models.Model):
    products_id=models.IntegerField()
    product_name=models.CharField(max_length=50)
    category_id=models.IntegerField()
    list_price=models.IntegerField()
    supplier_id=models.IntegerField()

class Orders(models.Model):
    order_id=models.IntegerField()
    staff_id=models.IntegerField()
    order_status=models.IntegerField()
    order_date=models.DateField()

class Order_items(models.Model):
    item_id=models.IntegerField()
    order_id=models.IntegerField()
    quantity=models.IntegerField()
    list_price=models.IntegerField()

class Suppliers(models.Model):
    suppliers_id=models.IntegerField()
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.IntegerField()
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    zip_code=models.IntegerField()

class Categories_product(models.Model):
    category_id=models.IntegerField()
    category_description=models.CharField(max_length=100)
    category_name=models.CharField(max_length=50)

class Stocks(models.Model):
    product_id=models.IntegerField()
    quantity=models.IntegerField()
    store_id=models.IntegerField()
    
