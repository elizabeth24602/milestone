from django.urls import path, include
from django.contrib import admin
from accounts import urls as urls_accounts
from products import urls as urls_products
# Made these accessible and tied them up
from home.views import home, about, gallery, contact, favourites
from blog.views import blog
from cart import urls as urls_cart
from checkout import urls as urls_checkout
from search.views import do_search
from products.views import all_products
from django.views import static
from .settings import MEDIA_ROOT


urlpatterns = [
    path('admin/', admin.site.urls),
    # remove / at the start of the route.
    # Otherwise you will have www.yourwebsite.com//gallery with 2 /
    # path('/gallery', all_products, name='gallery'),
    path('gallery', all_products, name='gallery'),

    # URLs you want direct form the directory.
    # get the url you want, Use and imported function - See top of page
    path('', home, name='home'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('search/', do_search, name='search'),
    path('favourites', favourites, name='favourites'),
    path('blog', blog, name='blog'),

    # additional APP urls
    path('accounts/', include(urls_accounts)),
    path('products/', include(urls_products)),
    path('cart/', include(urls_cart)),
    path('checkout/', include(urls_checkout)),
    path('media/<path:path>', static.serve, {'document_root': MEDIA_ROOT }),
]
