from django.contrib import admin
from django.urls import path, include
from users.views import schema_view

urlpatterns = [
    path('', schema_view),
    path('admin/', admin.site.urls),
    path('api/auth/', include('users.urls')),
    path('api/products/', include('products.urls'))
]
