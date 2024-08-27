from django.shortcuts import render
from movies.models import movies_post
<<<<<<< HEAD
=======
from posts.models import Post, Comment
>>>>>>> movies

# Create your views here.
def movies_list(request):
    posts = movies_post.objects.all()
    context = {"posts": posts}
    return render(request, "movies/movies.html", context)


def movies_detail(request, pk):
<<<<<<< HEAD
    post = movies_post.objects.get(id=pk)

    context = {"post": post}
=======
    m_post = movies_post.objects.get(id=pk)
    p_post = Post.objects.all()
>>>>>>> movies

    context = {
        "m_post": m_post
        }
    return render(request, "movies/movies_detail.html", context)
