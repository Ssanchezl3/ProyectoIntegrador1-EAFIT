from django.urls import path
from .views import product_list
from .views import product_search
from .views import news_list
from .views import product_list, product_search, news_list



urlpatterns = [
    path('', product_list, name='product_list'),
    path('', product_search, name='product_search'),
    path('', news_list, name='news_list')
]
