from django.shortcuts import render, redirect
from posts.models import Post, Comment
from movies.views import movies_detail

# Create your views here.

def feeds(request):
    # 요청(request)으로부터 사용자 정보를 사져옴
    user = request.user

    # 가져온 사용자가 "로그인 했는지" 여부를 가져옴
    is_authenticated = user.is_authenticated

    # 요청에 포함된 사용자가 로그인하지 않은 경우
    if not is_authenticated:
        # /users/login/ URL 로 이동시킴
        return redirect("/users/login/")
    

    # 모든 글 목록을 템플릿으로 전달
    posts = Post.objects.all()             
    context = {
        "posts" : posts
    }
    return render(request, "posts/feeds.html", context)

def detail(request):
    posts = Post.objects.all()             
    context = {
        "posts" : posts
    }
    return render(request, "posts/detail.html", context)
    

def new(request):
    # print(request.POST) # POST 메서드로 전달된 데이터를 출력
    if request.method == "POST": # method 가 POST 일 때
        review = request.POST["review"]
        short_comment = request.POST["short_comment"]
   
        post = Post.objects.create(
            review = review,
            short_comment = short_comment,
        )
        return redirect(f"/posts/detail/{post.pk}/")
    
    return render(request, "posts/new.html")
