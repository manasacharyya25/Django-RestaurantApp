from rest_framework import serializers
from .models import Menu


class MenuSerializer(serializers.ModelSerializer):
    model = Menu
    fields = ['created', 'menu_item', 'price']