from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]


class RawProductForm(forms.Form):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={
        "placeholder": "Your title Brother"
    }))
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "class": "my-class",
                "rows": 20,
                "cols": 120,
            }
        ))
    price = forms.DecimalField(initial=20.00)
