

# Create your views here.
from django.shortcuts import render

def news_list(request):
    return render(request, 'news/news_list.html')  # Asegúrate de crear esta plantilla
