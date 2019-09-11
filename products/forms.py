from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={
        "placeholder": "Your title"
    }))
    description = forms.CharField(
        label='',
        required=False,
        widget=forms.Textarea(
            attrs={
                "class": "my-class",
                "rows": 20,
                "cols": 120,
                "placeholder": "Description"
            }
        ))
    price = forms.DecimalField(initial=20.00)
    email = forms.EmailField()

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
            'summary'
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if "CFE" in title:
            return title
        else:
            raise forms.ValidationError("This is not valid title")

    def clean_price(self, *args, **kwargs):
        price = self.cleaned_data.get("price")
        if price > 10:
            return price
        else:
            raise forms.ValidationError("The price should be greater than $10")

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        if not email.endswith("edu"):
            raise forms.ValidationError("This is not valid email")


class RawProductForm(forms.Form):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={
        "placeholder": "Your title Brother"
    }))
    description = forms.CharField(
        label='',
        required=False,
        widget=forms.Textarea(
            attrs={
                "class": "my-class",
                "rows": 20,
                "cols": 120,
                "placeholder": "Description"
            }
        ))
    price = forms.DecimalField(initial=20.00)
