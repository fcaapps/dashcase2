from django.conf.urls import url
from .views import macropack

urlpatterns = [
    url('', macropack, name='macropack'),
]