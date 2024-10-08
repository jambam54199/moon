from django.shortcuts import render, redirect, get_object_or_404
from posts.models import Post, Comment, HashTag
from posts.forms import PostForm, CommentForm
from movies.views import movies_detail
from django.urls import reverse
from users.models import User
from movies.models import movies_post

# Create your views here.

def feeds(request):
    # 요청(request)으로부터 사용자 정보를 사져옴
    user = request.user

    # 가져온 사용자가 "로그인 했는지" 여부를 가져옴
    is_authenticated = user.is_authenticated

    # 요청에 포함된 사용자가 로그인하지 않은 경우
    if not is_authenticated:
        # /users/login/ URL 로 이동시킴
        return redirect("users:login")
    

    # 모든 글 목록을 템플릿으로 전달
    posts = Post.objects.all()     

    context = {
        "posts" : posts
    }

    return render(request, "posts/feeds.html", context)

def detail(request, post_id):
    posts = get_object_or_404(Post, pk = post_id)             
    context = {
        "posts" : posts,
    }
    return render(request, "posts/detail.html", context)
    

def new(request, pk):
    # movies_post에서 id=pk인 값 가져오기 pk로 받아왔으면 url에 넘겨줄 때 pk로 넘겨줘야 한다. 
    movies = movies_post.objects.get(id=pk)

    if request.method == "POST":
        
        # request.POST 로 온 데이터("review, short_comment")는 PostForm 으로 처리
        form = PostForm(request.POST)

        if form.is_valid():
            # Post 의 "user" 값은 request 에서 가져와 자동 할당
            post = form.save(commit=False)
            post.user = request.user
            post.save()

            # post.save()와 중복되는 구조
                # review = request.POST.get("review")
                # short_comment = request.POST.get("short_comment")

                # post = Post.objects.create(
                #     review = review,
                #     short_comment = short_comment,
                #     )

            # "tags" 에 전달된 문자열을 분리해 HashTag 생성
            tag_string = request.POST.get("tags")

            # tag는 나중에 추가로 받겠다. 부가적인 요소임을 명시.
            if tag_string:
                tag_name_list = [tag_name.strip() for tag_name in tag_string.split(",")]

                for tag_name in tag_name_list:
                    tag, _ = HashTag.objects.get_or_create(
                        name = tag_name,
                    )
                    # get_or_create 로 생성하거나 가져온 HashTag 객체를 Post 의 tags 에 추가
                    post.tags.add(tag)

            # 피드페이지로 이동하여 생성된 Post의 위치로 스크롤되도록 함
            return redirect(f"/posts/{post.id}/")

    # GET 요청일 때는 빈 form 을 보여주도록 함
    else:
        form = PostForm()

    context = {
        "movies" : movies,
        "form" : form
    }

    return render(request, "posts/new.html", context)

def tags(request, tag_name):
    try:
        tag = HashTag.objects.get(name = tag_name)
    
    except HashTag.DoesNotExist:
        # tag_name 에 해당하는 HashTag를 찾지 못한 경우 빈 QuerySet 을 돌려줌
        posts = Post.objects.none()

    else:
        # tags(M2M 필드)에 찾은 HashTag 객체가 있는 Post 들을 필터링
        posts = Post.objects.filter(tags = tag)

    # context 로 Template 에 필터링 된 Post QuerySet 을 넘겨주며
    # 어떤 tag_name 으로 검색했는지도 넘겨줌
    context = {
        "tag_name" : tag_name,
        "posts" : posts,
    }
    return render(request, "posts/tags.html", context)

def post_like(request, post_id):
    post = Post.objects.get(id = post_id) # 입력받은 id에 해당하는 게시글
    user = request.user # 누가 눌렀는지

    # 사용자가 이미 좋아요를 누른 Post라면
    if user.like_posts.filter(id = post.id).exists():
        # 좋아요 삭제
        user.like_posts.remove(post)
    
    else:
        user.like_posts.add(post)
    
    # next 로 값이 전달되었다면 해당 위치로, 전달되지 않았다면 피드페이지에서 해당 Post 위치로 이동
    url_next = request.GET.get("next") or reverse("posts:feeds") + f"#post-{post.id}"
    # 왼쪽값이 True일 경우 왼쪽값, False일 경우 오른쪽값
    return redirect(url_next)
