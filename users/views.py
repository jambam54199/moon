from django.shortcuts import render, redirect

# Create your views here.
def login_view(request):
    return render(request, "users/login.html")