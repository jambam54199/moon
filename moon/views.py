# djgram/views.py

from django.shortcuts import render, redirect

def main(request):

    if request.user.is_authenticated:
        return redirect("/posts/feeds/")
    
    else:
        return redirect("/users/login/")