from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from iddashop import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('iddashop.main.urls')),
    path('accounts/', include('iddashop.accounts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
