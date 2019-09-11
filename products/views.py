# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm, RawProductForm
from django.http import HttpResponse


def product_list_view(request):
    query_set = Product.objects.all()
    context = {
        "object_list": query_set
    }
    return render(request, 'products/product_list.html', context)


def product_delete_view(request, my_id):
    # obj = Product.objects.get(id=my_id)
    obj = get_object_or_404(Product, id=my_id)
    print("The object is ", obj)
    if request.method == "POST":
        # confirming the delete
        obj.delete()
        return redirect('../../')  # redirect pages
    context = {
        'object': obj
    }
    return render(request, 'products/product_delete.html', context)


def dynamic_lookup_view(request, my_id):
    # obj = Product.objects.get(id=my_id)
    obj = get_object_or_404(Product, id=my_id)
    if request.method == "POST":
        obj.delete()
    context = {
        'object': obj
    }
    return render(request, 'products/product_detail.html', context)


def render_initial_data(request):
    initial_data = {
        "title": "My awesome title",
        "description": "This is dummy description through initial data"
    }
    obj = Product.objects.get(id=1)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        "form": form
    }
    return render(request, 'products/product_create.html', context)


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