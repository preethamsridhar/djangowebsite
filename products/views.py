# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Product
from .forms import ProductForm, RawProductForm
from django.http import HttpResponse


# Create your views here.
def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        "form": form
    }
    return render(request, "products/product_create.html", context)


# Create your views here.
# def product_create_view(request):
#     # print(request.GET)
#     if request.method == "POST":
#         print(request.POST)
#         print("title: ", request.POST.get('title'))
#         context = {}
#         return render(request, "products/product_create.html", context)
#     else:
#         return HttpResponse("Hi")


# # Create your views here.
# def product_create_view(request):
#     form = RawProductForm()
#     if request.method == "POST":
#         form = RawProductForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             Product.objects.create(**form.cleaned_data)
#             form = RawProductForm()
#         else:
#             print(form.errors)
#     context = {
#         "form": form
#     }
#     return render(request, "products/product_create.html", context)


def product_detail_view(request):
    obj = Product.objects.get(id=1)
    context = {
        "object": obj
    }
    return render(request, "products/product_detail.html", context)