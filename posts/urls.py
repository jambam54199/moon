from django.urls import path
from posts import views

urlpatterns = [
    path("feeds/", views.feeds),
]