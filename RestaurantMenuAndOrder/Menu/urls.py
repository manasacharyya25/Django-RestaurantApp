from django.urls import path
from .views import MenuView
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('snippet/', MenuView.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)