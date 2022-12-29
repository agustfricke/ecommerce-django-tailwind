from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('products.urls')),
    path('users/', include('users.urls')),
    path('orders/', include('orders.urls')),
    path('administrador/', include('administrador.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
