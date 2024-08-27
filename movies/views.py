from django.shortcuts import render
from movies.models import movies_post
from posts.models import Post, Comment

# Create your views here.
def movies_list(request):
    m_posts = movies_post.objects.all()
    line = movies_post.objects.get()
    context = {
        "m_posts": m_posts,
        "line" : line,
        }
    return render(request, "movies/movies.html", context)


def movies_detail(request, pk):
    m_post = movies_post.objects.get(id=pk)
    posts = Post.objects.all()

    context = {
        "m_post": m_post,
        "posts" : posts,
        }
    return render(request, "movies/movies_detail.html", context)
