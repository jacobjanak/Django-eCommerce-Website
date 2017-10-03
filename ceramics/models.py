from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=60)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='static/ceramics/images/', null=True, blank=True)

    def __str__(self):
        return f'{self.name} - ${self.price}'
