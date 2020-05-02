from .views import do_search
from django.urls import path

urlpatterns = [
    path('', do_search, name='search'),
]
