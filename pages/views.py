# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home_view(request):
    print(request.user)
    # return HttpResponse("<h1>Hello World</h1>") # String of html code
    return render(request, 'home.html', {})


def contact_view(request):
    # return HttpResponse("<h1>Contact Page</h1>")
    return render(request, 'contact.html', {})


def about_view(request):
    # return HttpResponse("<h1>Contact Page</h1>")
    context_text = {
        "my_text": "I am a Django Developer",
        "my_number": 123456,
        "country": [
            "usa",
            "india",
            "srilanka"
        ]
    }
    return render(request, 'about.html', context_text)