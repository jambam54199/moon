from django.urls import path
from users import views

urlpatterns = [
    path("login/", views.login_view),
    path("logout/", views.logout_view),
    path("signup/", views.signup),
]