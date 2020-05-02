from django.urls import path, include
from django.contrib import admin
from django.urls import path
from accounts import urls as urls_accounts
from products import urls as urls_products
from cart import urls as urls_cart
from search.views import do_search
from products.views import all_products
from django.views import static
from .settings import MEDIA_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', all_products, name='index'),
    path('accounts/', include(urls_accounts)),
    path('products/', include(urls_products)),
    path('cart/', include(urls_cart)),
    path('search/', do_search, name='search'),
    path('media/<path:path>', static.serve, {'document_root': MEDIA_ROOT }),
]
