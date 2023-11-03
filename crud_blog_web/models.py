from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=150, blank=False, unique=False)
    year = models.PositiveSmallIntegerField(default=2023)

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    in_stock = models.BooleanField(default=True)
