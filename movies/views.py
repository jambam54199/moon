from django.shortcuts import render
from movies.models import movies_post
from posts.models import Post
import random


# Create your views here.
def movies_list(request):
    m_posts = movies_post.objects.all()
    line = movies_post.objects.all()

    ran = random.choice(line)

    context = {
        "m_posts": m_posts,
        "line": line,
        "ran": ran,
    }
    return render(request, "movies/movies.html", context)


def movies_detail(request, pk):
    # movies_detail.html에 넘겨주는 movies_post의 모든 정보는 m_post 로 받는다.
    # m_post 는 movies_post에서 id=pk인 값만 찾아서 get으로 가져온다.
    m_post = movies_post.objects.get(id=pk)

    # 영화 관련 글 목록 조회
    posts = m_post.post_set.all().order_by("-id")

    context = {
        "m_post": m_post,
        "posts": posts,
    }
    # movies_detail.html에 넘겨주는 pk값의 이름은 pk임을 명시했다.
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
