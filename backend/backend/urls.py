from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('products.urls')),
    path('users/', include('users.urls')),
    path('orders/', include('orders.urls')),
    path('admin/', include('admin.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
