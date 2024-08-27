from django.shortcuts import render
from movies.models import movies_post


# Create your views here.
def movies_list(request):
    posts = movies_post.objects.all()
    context = {"posts": posts}
    return render(request, "movies/movies.html", context)


def movies_datail(request, pk):
    post = movies_post.objects.get(id=pk)

    context = {"post": post}

    return render(request, "movies/movies_detail.html", context)
