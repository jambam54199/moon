from django.shortcuts import render, redirect, get_object_or_404
from users.forms import LoginForm, SignupForm
from django.contrib.auth import authenticate, login, logout
from users.models import User

# Create your views here.
def login_view(request):
    # 이미 로그인 되어 있는 경우 -> 피드 페이지로
    if request.user.is_authenticated:
            return redirect("posts:feeds")
        
    # POST 방식으로 요청이 온 경우(로그인 시도)
    if request.method == "POST":
        # LoginForm 인스턴스를 만들며, 입력 데이터는 request.POST 를 사용
        form = LoginForm(data = request.POST)

        # LoginForm 에 들어온 데이터가 적절한지 유효성 검사
        print("form.is_valid():", form.is_valid())

        # LoginForm 에 전달된 데이터가 유효하다면
        if form.is_valid():
            # username과 password 값을 가져와 변수에 할당
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            # usernam, password 에 해당하는 사용자가 있는지 검사
            user = authenticate(username = username, password = password)

            # 해당 사용자가 존재한다면
            if user:
                # 로그인 처리 후, 피드 페이지로 redirect
                login(request, user)
                return redirect("posts:feeds")
            
            # 해당 사용자가 없다면 form에 에러 추가
            else:
                form.add_error(None, "입력한 사용자가 존재하지 않습니다.")

        # 어떤 이유든, 실패한 경우라면 다시 LoginForm을 사용한 로그인 페이지 렌더링
        context = {
            "form" : form,
        }
        return render(request, "users/login.html", context)
    
    else:
        # LoginForm 인스턴스를 생성
        form = LoginForm()

        # 생성한 LoginForm 인스턴스를 템플릿에 "form"이라는 키로 전달
        context = {
            "form" : form,
        }
        return render(request, "users/login.html", context)
    
def logout_view(request):
    # logout 함수호출에 request를 전달
    logout(request)

    # logout 처리 후 로그인 페이지로
    return redirect("/users/login/")


def signup(request):
    if request.method == "POST":
        form = SignupForm(data = request.POST, files = request.FILES)

        # Form 에 에러가 없다면 form의 save() 메서드로 사용자를 생성
        if form.is_valid():        
            user = form.save()
            login(request, user)
            return redirect("posts:feeds")
            
    # GET 요청에는 빈 Form을 보여줌
    else:
        # SignupForm 인스턴스를 생성, Template에 전달
        form = SignupForm()

    # context로 전달되는 form은 2가지 경우 존재
    # 1. POST 요청에서 생성된 form 이 유효하지 않은 경우 -> 에러를 포함한 form이 사용자에게 보여짐
    # 2. GET 요청으로 빈 form이 생성된 경우 -> 빈 form이 사용자에게 보여짐
    context = {
            "form" : form,
        }
    return render(request, "users/signup.html", context)
