# djgram/views.py

from django.shortcuts import render, redirect

def main(request):
    # 로그인 되어있다면 피드 페이지로
    if request.user.is_authenticated:
        return redirect("/posts/feeds/")
    # 로그인 안되어있다면 로그인 페이지로
    else:
        return redirect("/users/login/")