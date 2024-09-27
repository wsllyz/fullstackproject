from django.db import models

# Create your models here.

class Pizza(models.Model):
    nome = models.TextField(max_length=100)
    ingredientes = models.TextField(max_length=100)
    preco = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self) -> str:
        return self.name