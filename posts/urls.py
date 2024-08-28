from django.urls import path
from posts import views

app_name = "posts"
urlpatterns = [
    path("feeds/", views.feeds, name = "feeds"),
    # view의 new함수에서 pk값을 pk로 지정했으므로 int:pk로 넣어준다.
    path("new/<int:pk>/", views.new, name = "new"),
    # view의 tag함수에서 pk값을 tag_name으로 지정했으므로 str:tag_name으로 넣어준다.
    path("tags/<str:tag_name>/", views.tags, name = "tags"),
    path("<int:post_id>/", views.detail, name = "detail"),
    path("<int:post_id>/like/", views.post_like, name = "post_like"),
]