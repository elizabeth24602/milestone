from django.urls import path
from .views import view_cart, add_to_cart, adjust_cart

urlpatterns = [
    path(' ', view_cart, name='view_cart'),
    path('add(path:<id>)', add_to_cart, name='add_to_cart'),
    path('adjust(path:<id>)', adjust_cart, name='adjust_cart'),
]