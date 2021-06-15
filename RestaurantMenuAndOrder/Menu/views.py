from rest_framework import generics
from .models import Menu
from .serializers import MenuSerializer


class MenuListView(generics.ListAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class MenuCreateView(generics.CreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class MenuDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
