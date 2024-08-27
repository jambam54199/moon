from django.urls import path
from posts import views

app_name = "posts"
urlpatterns = [
    path("feeds/", views.feeds, name = "feeds"),
    path("new/", views.new, name = "new"),
    path("detail/", views.detail, name = "detail"),
<<<<<<< HEAD
    path("new/", views.new, name = "new")
=======
    path("tags/<str:tag_name>/", views.tags, name = "tags"),
    path("<int:post_id>/", views.detail, name = "detail"),
    path("<int:post_id>/like/", views.post_like, name = "post_like"),
>>>>>>> d3d8d4c410294cd867ff0379f08ba0cfb1173136
]