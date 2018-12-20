from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from hello.models import Person,User
# Create your views here.


def index(request):
    return render(request,'hello/login.html')

#页面显示数据
def show_data(request):
    string = "我正在学习字符串在页面显示"
    languageList=["java","php","python",'html','c#']
    userDict={'name':'zhuly','age':26}
    return render(request,'hello/show_data.html',{'string':string,'lanList':languageList,'userDict':userDict})

# 采用 /add/?a=4&b=5 这样GET方法进行
def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a)+int(b)
    return HttpResponse(str(c))

#采用 /add/3/4/ 这样的网址的方式
def add2(request, a, b):
    c = int(a)+int(b)
    return HttpResponse(str(c))

#重定向
def old_add2_redirect(request,a,b):
    return HttpResponseRedirect(reverse('add2',args=(a,b)))

def login(request):
    user= User.objects.get(name=request.POST['name'])
    if user.pwd==request.POST['pwd']:
        sess=request.session[user.name]
        if sess:
            return HttpResponse("你已经登陆")
        else:
            request.session[user.name]=user.name
            return HttpResponse("登陆成功")
    else:
        return HttpResponse("账号和密码匹配")


