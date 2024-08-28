from django.shortcuts import render, redirect, get_object_or_404
from posts.models import Post, Comment, HashTag
from posts.forms import PostForm, CommentForm
from django.views.decorators.http import require_POST
from movies.views import movies_detail
from django.urls import reverse
from users.models import User

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

def detail(request):
    posts = Post.objects.all()             
    context = {
        "posts" : posts,
    }
    return render(request, "posts/detail.html", context)
    

@require_POST
def new(request):
    if request.method == "POST":
        # request.POST 로 온 데이터("content")는 PostForm 으로 처리
        form = PostForm(request.POST)

        if form.is_valid():
            # Post 의 "user" 값은 request 에서 가져와 자동 할당
            post = form.save(commit=False)
            post.user = request.user
            post.save()

            # Post 를 생성한 후
            # request.FILES.getlist("images") 로 전송된 이미지들을 순회하며
            # PostImage 객체를 생성
            # for image_file in request.FILES.getlist("images"):
            #     # request.FILES 또는 request.FILES.getlist() 로 가져온 파일은
            #     # Model 의 ImageField 부분에 곧바로 할당
            #     PostImage.objects.create(
            #         post = post,
            #         photo = image_file,
            #     )

            # "tags" 에 전달된 문자열을 분리해 HashTag 생성
            tag_string = request.POST.get("tags")

            if tag_string:
                tag_name_list = [tag_name.strip() for tag_name in tag_string.split(",")]

                for tag_name in tag_name_list:
                    tag, _ = HashTag.objects.get_or_create(
                        name = tag_name,
                    )
                    # get_or_create 로 생성하거나 가져온 HashTag 객체를 Post 의 tags 에 추가
                    post.tags.add(tag)

            # 모든 PostImage 와 Post 의 생성이 완료되면
            # 피드페이지로 이동하여 생성된 Post 의 위치로 스크롤되도록 함
            url = reverse("posts") + f"#post-{post.id}"
            return redirect(url)

    # GET 요청일 때는 빈 form 을 보여주도록 함
    else:
        form = PostForm()

    context = {
        "form" : form
    }

    return render(request, "posts/new.html", context)

def tags(request, tag_name):
    try :
        tag = HashTag.objects.get(name = tag_name)

    except HashTag.DoesNotExist:
        posts = Post.objects.none()

    else:
        # tags (M2M 필드)에 찾은 HashTag 객체가 있는 Post들을 필터링
        posts = Post.objects.filter(tags = tag)
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
