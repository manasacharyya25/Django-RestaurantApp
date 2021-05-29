from django.http.response import HttpResponse
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def product_view(*args, **kwargs):
    return HttpResponse("<h1>Hello Products</h1>")
