from django.db import models

from django.contrib.auth.models import User

from shop.models import Product, Category


class WishList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.product}"

