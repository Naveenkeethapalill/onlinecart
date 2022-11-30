from django.db import models


class Product(models.Model):
    item=models.CharField(max_length=20)
    price=models.FloatField()
    image=models.CharField(max_length=200)

    def __str__(self):
        return self.item