from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def viewteste(request):
    return HttpResponse("Testando view")

def viewteste2(request):
    return HttpResponse("Testando view (2)")

def viewhtml(request):
    return render(request, 'teste.html')