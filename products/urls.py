from django.urls import path
from .views import productsView, productUpdate
urlpatterns = [
    path('', productsView.as_view(),  name='productsView'),
    path('<int:pk>/', productUpdate.as_view(),  name='productsView'),
]
