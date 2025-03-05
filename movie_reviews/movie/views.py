from django.shortcuts import render
from .models import Product
from .models import Article
from django.http import HttpResponse


# Create your views here.
def product_list(request):
    products = Product.objects.all()  # Obtener todos los productos
    return render(request, 'movie/product_list.html', {'products': products})

def product_search(request):
    render(request, 'movie/product_list.html')

def news_list(request):
    return HttpResponse("Noticias")
