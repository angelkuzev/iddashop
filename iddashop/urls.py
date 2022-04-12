from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from iddashop import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('iddashop.main.urls')),
    path('accounts/', include('iddashop.accounts.urls')),
]
