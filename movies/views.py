from django.shortcuts import render
from movies.models import movies_post
from posts.models import Post, Comment


# Create your views here.
def movies_list(request):
    posts = movies_post.objects.all()
    context = {"posts": posts}
    return render(request, "movies/movies.html", context)


def movies_detail(request, pk):
    m_post = movies_post.objects.get(id=pk)
    context = {
        "m_post": m_post
        }
    return render(request, "movies/movies_detail.html", context)
