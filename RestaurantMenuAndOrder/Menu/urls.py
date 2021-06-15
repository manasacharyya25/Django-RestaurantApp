from django.urls import path
from .views import MenuListView, MenuDetailView, MenuCreateView
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('snippet/', MenuListView.as_view()),
    path('create_snippet/', MenuCreateView.as_view()),
    path('snippet/<int:pk>', MenuDetailView.as_view())

]

urlpatterns = format_suffix_patterns(urlpatterns)
