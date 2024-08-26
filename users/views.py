from django.shortcuts import render, redirect
from users.forms import LoginForm
from django.contrib.auth import authenticate, login

# Create your views here.
def login_view(request):
    # 이미 로그인 되어있는 경우
    if request.user.is_authenticated:
        return redirect("/posts/feeds/")
    
    if request.method == "POST":
        # LoginForm 인스턴스 생성, 입력 데이터는 request.POST
        form = LoginForm(data = request.POST)

        # LoginForm에 전달된 데이터가 유효하다면
        if form.is_valid():
            # username, password 값 가져와 변수에 할당
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            # username, password 에 해당하는 사용자 있는지
            user = authenticate(username = username, password = password)

            # 해당 사용자가 존재한다면
            if user:
                login(request, user)
                return redirect("/posts/feeds/")

            # 해당 사용자가 없다면
            else:
                print("로그인에 실패하였습니다.")

        # 어쨌든 실패했다면 다시 로그인으로 렌더링
        # 생성한 LoginForm 인스턴스를 템플릿에 전달
        context = {
            "form" : form,
        }
        return render(request, "users/login.html", context)
    
    else:
        form = LoginForm()

        context = {
            "form" : form,
        }
        return render(request, "users/login.html", context)