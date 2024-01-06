from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('auth_app.urls', namespace='auth_app')),
    path('', include('pages.urls', namespace='pages_app')),
    path('clientes/', include('clientes.urls', namespace='clientes_app')),
]