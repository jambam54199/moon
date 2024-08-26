from django.shortcuts import render, redirect

# Create your views here.

def feeds(request):
    return render(request, "posts/feeds.html")