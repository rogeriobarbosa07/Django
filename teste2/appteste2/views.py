from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def viewteste(request):
    return HttpResponse("Testando view")