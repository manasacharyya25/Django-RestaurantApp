from django.db import models


# Create your models here.
class Menu(models.Model):
    created = models.DateField(auto_now_add=True)
    item_name = models.TextField(max_length=10)
    item_price = models.IntegerField()

    class Meta:
        ordering = ['created']
