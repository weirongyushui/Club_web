from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
def Login(request):
    return render(request,"html/Login.html")
def index(request):
    return render(request,"html/index.html")
def borrow(request):
    return render(request,"html/borrow.html")
def administrators(request):
    return render(request,"html/administrators.html")
def users(request):
    return render(request,"html/users.html")
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # 替换'home'为您的主页URL名称
        else:
            error_message = '用户名或密码不正确'
            return render(request, 'Login.html', {'error_message': error_message})
    return render(request, 'html/Login.html')