from django.db import models
from django.core.validators import MinValueValidator


class Product(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True
    )
    description = models.TextField()
    quantity = models.IntegerField(
        validators=[MinValueValidator(0)]
    )
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='products'  # все продукты в категории будут доступны через поле products
    )
    price = models.FloatField(
        validators=[MinValueValidator(0.0)]
    )

    def __str__(self):
        return f'{self.name.title()}: {self.description[:20]}'


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True
    )

    def __str__(self):
        return f'{self.name.title()}'


class News(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return f'{self.title.title()}: {self.text[:20]}...'
