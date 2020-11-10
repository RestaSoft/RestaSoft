from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Stores(models.Model):


    store_name = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.IntegerField()

    def __str__(self):
        return str(self.store_name)

    class Meta:
        verbose_name_plural = 'Stores'



class Permission(models.Model):

    LIST_PERMISSION = [

        ('Adm', 'Administrativo'),
        ('Chef', 'Cocinero'),
        ('Mes', 'Mesero'),
    ]

    name_permission = models.CharField(choices=LIST_PERMISSION, max_length=50, null=True)

    def __str__(self):
        return str(self.name_permission)

    class Meta:
        verbose_name_plural = 'Permissions'



class Staffs(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    phone = models.IntegerField(blank=True, null=True)
    stores = models.ForeignKey(Stores, on_delete=models.CASCADE, null=True)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE, null=True)
    active = models.BooleanField(('active'), default=True, null=True)
    imagen = models.ImageField(
        upload_to = 'users/pictrues',
        blank= True,
        null = True)

    def __str__(self):
        return str(self.user.username)
    
    class Meta:
        verbose_name_plural = 'Staffs'
 


class CategoriesProduct(models.Model):
    category_description = models.CharField(max_length=100)
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.category_name)



class Suppliers(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.IntegerField()

    def __str__(self):
        return str(self.last_name)

    class Meta:
        verbose_name_plural = 'Suppliers'

    


class Products(models.Model):
    product_name = models.CharField(max_length=50)
    categoriesproduct = models.ForeignKey(CategoriesProduct, on_delete=models.CASCADE)
    list_price = models.IntegerField()
    suppliers = models.ForeignKey(Suppliers, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.product_name)

    class Meta:
        verbose_name_plural = 'Products'




class Orders(models.Model):
    staffs = models.ForeignKey(Staffs, on_delete=models.CASCADE)
    order_status = models.IntegerField()
    order_date = models.DateField()

    def __str__(self):
        return str(self.order_date, self.order_status)

    class Meta:
        verbose_name_plural = 'Orders'




class ItemsOrder(models.Model):
    orders = models.ForeignKey(Orders, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    list_price = models.IntegerField()

    def __str__(self):
        return str(self.quantity)

    class Meta:
        verbose_name_plural = 'Items Order'




class Stocks(models.Model):
    products = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    stores = models.ForeignKey(Stores, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.quantity)

    class Meta:
        verbose_name_plural = 'Stocks'

