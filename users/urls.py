from django.urls import path
from .views import LoginView, LogoutView, signupView


urlpatterns = [
    path('login/', LoginView.as_view(),  name="LogInAPI"),
    path('logout/', LogoutView.as_view(), name="LogoutAPI"),
    path('signup/', signupView.as_view(),  name="signupAPI"),
]
