from rest_framework import generics
from .models import Menu
from .serializers import MenuSerializer
from rest_framework.permissions import IsAuthenticated


class MenuListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class MenuDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
