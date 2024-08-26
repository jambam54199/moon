from django.shortcuts import render, redirect
from posts.models import Post

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