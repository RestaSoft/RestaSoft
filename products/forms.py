from django.forms import ModelForm
from users.models import Products, CategoriesProduct

class ProductsForm(ModelForm):
    class Meta:
        model = Products
        fields = '__all__'