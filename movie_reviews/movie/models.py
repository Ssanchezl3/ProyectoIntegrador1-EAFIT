from django.db import models

# Create your models here.
class Product(models.Model):
    PRODUCT_TYPES = [
        ('agricola', 'Agrícola'),
        ('ganado', 'Ganado'),
    ]

    name = models.CharField(max_length=200)  # Nombre del producto
    description = models.TextField()  # Descripción
    product_type = models.CharField(max_length=10, choices=PRODUCT_TYPES)  # Tipo de producto
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Precio
    available = models.BooleanField(default=True)  # Disponibilidad

    def __str__(self):
        return self.name
    
    
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='news_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
