from django.shortcuts import render

# Create your views here.

from django.http.response import HttpResponse

def home(request):
    return HttpResponse('hello world!')
