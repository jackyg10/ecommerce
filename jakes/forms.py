from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name',  'price', 'image','description',]
        widgets = {
    'title': forms.TextInput(attrs={
        'class': 'form-control form-control-sm'
    }),
}

