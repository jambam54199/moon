from django.urls import path
from posts import views

app_name = "posts"
urlpatterns = [
    path("feeds/", views.feeds, name = "feeds"),
    path("detail/", views.detail, name = "detail"),
    path("detail/<int:pk>", views.detail, name = "post_add"),
    path("new/", views.new, name = "new")
]