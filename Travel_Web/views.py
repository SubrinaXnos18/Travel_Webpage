from django.shortcuts import render


def user(request):
    return render(request,'user_login.html')

def package(request):
    return render(request,'package.html')