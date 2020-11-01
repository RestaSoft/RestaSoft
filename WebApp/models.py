from django.db import models
#from django.contrib.auth.models import Restaurate

# Create your models here.
class Stores(models.Model):
    store_name = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Store'


class Permission(models.Model):
    name_permission = models.CharField(max_length=50)


class Staffs(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField()
    stores = models.ForeignKey(Stores, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Staff'


class CategoriesProduct(models.Model):
    category_description = models.CharField(max_length=100)
    category_name = models.CharField(max_length=50)


class Suppliers(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Supplier'


class Products(models.Model):
    product_name = models.CharField(max_length=50)
    categories_product = models.ForeignKey(CategoriesProduct, on_delete=models.CASCADE)
    list_price = models.IntegerField()
    suppliers = models.ForeignKey(Suppliers, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Product'


class Orders(models.Model):
    staffs = models.ForeignKey(Staffs, on_delete=models.CASCADE)
    order_status = models.IntegerField()
    order_date = models.DateField()

    class Meta:
        verbose_name_plural = 'Order'


class ItemsOrder(models.Model):
    orders = models.ForeignKey(Orders, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    list_price = models.IntegerField()
    

class Stocks(models.Model):
    products = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    stores = models.ForeignKey(Stores, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Stock'