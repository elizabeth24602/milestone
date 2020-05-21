from django.urls import include, path
from .views import blog

urlpatterns = [
    path('blog/', blog, name='blog'),