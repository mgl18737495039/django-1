from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse,HttpResponsePermanentRedirect,HttpResponseRedirect
# Create your views here.
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session

from django.contrib.auth import authenticate,login,logout
from . import models


def register(request):
    if request.method=='GET':
        sorts = models.Sort.objects.all()

        print(sorts)

        return render(request,'register.html',{'sorts': sorts})
    elif request.method=="POST":

        username=request.POST["username"]
        userpwd = request.POST["userPassword"]
        userpwd_2 = request.POST["ag_userPassword"]
        useremail = request.POST["emaile"]
        nickname=request.POST['nickname']
        try :
            user=User.objects.get(username=username)
            return render(request,'register.html',{'error_code':-1,"error_msg":"此账号已存在"})
        except:
            try:
                nickname=User.User_file.objects.get(nickname=nickname)
                return render(request,'register.html',{'error_code':-2,"error_msg":"昵称已存在"})
            except:
                if userpwd!=userpwd_2:
                    return render(request, 'register.html', {'error_code': -3, "error_msg": "两次密码不一致"})
                user=User.objects.create_user(username=username,password=userpwd,email=useremail)
                userfile=models .User_file(nickname=nickname,user_file=user)
                user.save()
                userfile.save()
                return render(request,'login.html',{'error_code': 1, "error_msg": "使用新账号登录"})
def user_login(request):
    if request.method == 'GET':
        sorts = models.Sort.objects.all()

        return render(request, 'login.html', {'username':000 ,'sorts': sorts})
    elif request.method == "POST":
        username=request.POST['username']
        userpass= request.POST["userpass"]
        user=authenticate(username=username,password=userpass)
        if user is not None:
            login(request, user)


            request.session['username'] = username

            return redirect('/',{'request':request})
        else:

            return render(request,'login.html',{'error_code':-1,"error_msg":'账号密码不对'})
def user_logout(request):
    logout(request)
    response=HttpResponse()
    response.delete_cookie('username')
    return redirect('/')
def update_pwd(request):
    username = request.session.get("username")
    user_1=User.objects.get(username=username)

    if request.method == 'GET':
        sorts = models.Sort.objects.all()
        return render(request,'update_pwd.html',{
                       'username': request.session.get("username"), 'sorts': sorts, })
    elif request.method == "POST":

            pwd1 = request.POST['pwd1']
            pwd2 =request.POST['pwd2']
            if pwd1 != pwd2:
                return render(request, 'update_pwd.html', {'error_code': -1, "error_msg": '两次密码不同请重新输入'})
            else:

                user_1.set_password(pwd2)
                user_1.save()
                logout(request)
                response = HttpResponse()
                response.delete_cookie('username')
                return redirect('/')