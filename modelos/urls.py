from django.urls import path
from .views import modelos

urlpatterns = [
    path('', modelos, name="modelos"),
]
