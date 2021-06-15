from django.db import models


# Create your models here.
class Menu(models.Model):
    created = models.DateField(auto_now_add=True)
    menu_item = models.CharField(max_length=20)
    price = models.IntegerField(default=10)

    class Meta:
        ordering = ['created']
