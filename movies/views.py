from django.shortcuts import render
from movies.models import movies_post, FamousLine
from posts.models import Post
import random


# Create your views here.
def movies_list(request):
    m_posts = movies_post.objects.all().order_by("-id")
    line = FamousLine.objects.all()

    line_ran = random.choice(line)
    image_ran1 = random.choice(m_posts)
    image_ran2 = random.choice(m_posts)

    context = {
        "m_posts": m_posts,
        "line": line,
        "line_ran": line_ran,
        "image_ran1" : image_ran1,
        "image_ran2" : image_ran2,
    }
    return render(request, "movies/movies.html", context)


def movies_detail(request, pk):
    m_post = movies_post.objects.get(id=pk)

    # 영화 관련 글 목록 조회
    posts = m_post.post_set.all().order_by("-id")

    # 영화 별점

    context = {
        "m_post": m_post,
        "posts": posts,
    }
    return render(request, "movies/movies_detail.html", context)


def search(request):
    movies = movies_post.objects.all()
    keyword = request.GET.get("keyword", None)

    if keyword:
        movies = movies_post.objects.filter(title__contains=keyword)
    else:
        movies = movies_post.objects.none()

    context = {"movies": movies}

    return render(request, "movies/search.html", context)
