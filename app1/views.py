from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def func1 (request):
    return HttpResponse('Func1 view')

def func2 (response):
    return HttpResponse('func2 view')