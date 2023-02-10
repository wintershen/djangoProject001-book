from django.shortcuts import render, HttpResponse, redirect


def login1(request):
    return HttpResponse("OK")


def login(request):
    return render(request, "login.html")


def index(request):
    return render(request, "index1.html")


def main(request):
    return render(request, "main.html")


def try_login(request):
    error_msg = ""
    # print(request.POST)
    if request.method == "POST":
        username = request.POST['username']
        pwd = request.POST['pwd']
        print(username, pwd)
        if username == "winter" and pwd == "winter123456":
            return redirect("/index/")
        else:
            error_msg = "用户名或密码错误"
        return render(request, 'main.html', {'error_msg': error_msg})
