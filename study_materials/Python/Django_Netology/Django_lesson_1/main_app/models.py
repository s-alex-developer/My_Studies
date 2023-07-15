from django.db import models


class Product(models.Model):

    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):

        return f'Продукт: {self.name}, описание: {self.description}, стоимость: {self.price} руб.\n'