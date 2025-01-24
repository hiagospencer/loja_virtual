from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'index.html')

def loja(request):
    return render(request, 'loja.html')
