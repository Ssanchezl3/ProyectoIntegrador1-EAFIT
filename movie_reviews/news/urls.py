from django.urls import path
from .views import news_list  # Asegúrate de tener esta vista en views.py

urlpatterns = [
    path('', news_list, name='news_list'),
]
