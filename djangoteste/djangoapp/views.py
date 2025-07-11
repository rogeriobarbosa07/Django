from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the djangoapp index.")
    # Para acessá-la em um navegador, precisamos mapeá-la para uma URL