from django.urls import path
from movies import views

app_name = "movies"
urlpatterns = [
    path("post/", views.movies_list, name="movies_list"),
    path("movies/<int:pk>/", views.movies_detail, name="movies_detail"),
]
