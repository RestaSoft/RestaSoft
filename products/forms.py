from django.forms import ModelForm
from users.models import Products, CategoriesProduct
from django import forms

class ProductsForm(ModelForm):
    class Meta:
        model = Products
        fields = '__all__'
        imagen = forms.ImageField()

class CategoriesProductForm(ModelForm):
    class Meta:
        model = CategoriesProduct
        fields ='__all__'