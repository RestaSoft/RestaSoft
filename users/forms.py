''' User profile form '''

# Django
from users.models import Staffs, Stores, User
from django import forms
from django.forms import ModelForm
from .models import Stores


class StaffsForm(forms.Form):
    ''' Staffs Form '''
    class Meta:
        imagen = forms.ImageField()


class StoresForm(ModelForm):
    class Meta:
        model = Stores
        fields ='__all__'

class UserForm(ModelForm):
    class Meta:
        model = User
        fields ='__all__'

class PictureForm(forms.Form):
    image = forms.ImageField()

        