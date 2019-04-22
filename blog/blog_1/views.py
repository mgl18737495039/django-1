from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse,HttpResponsePermanentRedirect,HttpResponseRedirect
# Create your views here.
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session

from django.contrib.auth import authenticate,login,logout
from . import models


def register(request):
    if request.method=='GET':
        return render(request,'register.html',{})
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

        return render(request, 'login.html', {'username':000})
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