from django.contrib.auth.models import AbstractUser
from django.db import models

class Comprador(AbstractUser):
    telefono = models.CharField(max_length=15, blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="compradores_groups",
        blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="compradores_permissions",
        blank=True
    )

    def __str__(self):
        return self.username

