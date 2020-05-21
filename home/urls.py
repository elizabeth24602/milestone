from django.urls import include, path
from .views import home, about, gallery, contact, favourites

urlpatterns = [
    path('gallery/', all_products, name='gallery'),
    path('about/', about, name='about'),
    path('contact', contact, name='contact'),
    path('home/', home, name='home'),
    path('favourites/', favourites, name='favourites'),
    # path("home", include(urls_about)),   
]
