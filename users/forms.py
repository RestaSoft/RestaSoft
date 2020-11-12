''' User profile form '''

# Django
from django import forms

class StaffsForm(forms.Form):
    ''' Staffs Form '''
    class Meta:
        imagen = forms.ImageField()