from django.contrib import admin
from django.urls import path, include
from accounts import urls as urls_accounts

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include(urls_accounts)),
]
