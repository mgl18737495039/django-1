from django.shortcuts import render,redirect,reverse
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.sessions.models import Session
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import authenticate,login,logout
from . import models
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer ,SignatureExpired
# Create your views
def index(request):
    imgs=models.Img.objects.order_by("index")
    print(imgs)
    blogs=models.Blog.objects.all()
    return render(request,"index.html",{"imgs":imgs,'blogs':blogs})
def reader_login(request):
    if request.method=='GET':
        return render(request,"reader_login.html",{})
    elif request.method=="POST":
        username = request.POST['username']
        userpass = request.POST["password"]
        user = authenticate(username=username, password=userpass)
        if user is not None:
            login(request, user)

            request.session['username'] = username

            return redirect(reverse('book_guan:reader'))
        else:
            erro_msg='账号密码不对'
            return redirect(reverse("book_guan:reader_login"))
            # return render(request, 'login.html', {'error_code': -1, "error_msg": '账号密码不对'})
def register(request):

    if request.method == 'GET':
        return render(request, "register.html", {})
    elif request.method == "POST":

        username=request.POST["username"]
        password=request.POST["password"]
        password2=request.POST["password2"]
        college=request.POST["college"]
        number=request.POST["number"]
        email=request.POST["email"]
        try:
            user_cunzai=User.objects.get(username=username)
            return render(request, 'register.html', {'error_code': -2, "error_msg": "用户名已存在"})
        except:
            try:
                emile_user = User.objects.get(email=email)
                return render(request, 'register.html', {'error_code': -2, "error_msg": "邮箱已存在"})
            except:
                if password==password:
                    user1 = User.objects.create_user(username=username, password=password, email=email,is_active=False)
                    user_file=models.User_file(user_num_stu=number,user_college=college,user=user1)

                    user1.save()
                    user_file.save()
                    id=models.User_file.objects.get(user=user1).id
                    result=Serializer(settings.SECRET_KEY,300)
                    resultid=result.dumps({"user_id":id}).decode("utf-8")

                    send_mail("点击激活账户","<a href='http://127.0.0.1:8000/mgl/active/%s'>点击我</a>"%(resultid,),settings.DEFAULT_FROM_EMAIL,[email])
                    return render(request, 'reader_login.html', {})
                else:
                    return render(request, 'register.html', {'error_code': -2, "error_msg": "两次密码不相同已存在"})

def reader(request):

    username = request.session.get("username")


    return render(request, "reader.html", {"username": username})
def user_logout(request):
    logout(request)

    return redirect(reverse('book_guan:index'))
def reader_info(request):
    username = request.session.get("username")
    user1=User.objects.get(username=username)
    return render(request,"reader_info.html",{"user":user1})
def reader_modify(request):
    username = request.session.get("username")
    user1 = User.objects.get(username=username)
    if request.method=='GET':
        return render(request,"reader_modify.html",{})
    elif request.method=="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        college = request.POST["college"]
        number = request.POST["number"]
        email = request.POST["email"]
        if password==user1.password:

            user1.username = username
            user1.user_file.user_clolege = college
            user1.user_file.user_num_stu = number
            user1.email = email


            # user1.set_password(password)

            user1.save()
            user1.user_file.save()
            logout(request)

            return redirect(reverse("book_guan:reader_login"))
        else:
            user1.username = username
            user1.user_file.user_clolege = college
            user1.user_file.user_num_stu = number
            user1.email = email

            user1.set_password(password)

            user1.save()
            user1.user_file.save()
            logout(request)

            return redirect(reverse("book_guan:reader_login"))
def reader_query(request):
    if request.method=='GET':
        return render(request,"reader_query.html",{})
    elif request.method=="POST":
        chioce=request.POST['item']
        if chioce =='name':
            query=request.POST['query']
            books=models.Book_info.objects.filter(book_name__contains=query)
            if books==None:
                return render(request,'reader_query.html',{'e':'查询失败'})
            else:
                return render(request, 'reader_query.html', {'books': books})
        else:
            query=request.POST['query']
            books=models.Book_info.objects.filter(book_author__contains=query)
            if books==None:
                return render(request,'reader_query.html',{'e':'查询失败'})
            else:
                return render(request, 'reader_query.html', {'books': books})

def reader_book(request,id):
    if request.method=='GET':
        book=models.Book_info.objects.get(pk=id)
        readers=book.jieshu_set.all()
        return render(request,'reader_book.html',{'book':book,'readers':readers})
def jie(request,id):

    book = models.Book_info.objects.get(pk=id)
    if book.book_num>0:
        username = request.session.get("username")
        user1 = User.objects.get(username=username)
        jieshu=models.Jieshu(book=book,user=user1)
        jieshu_lishi = models.Jieshu_lishi(book=book, user=user1)
        jieshu.save()
        jieshu_lishi.save()
        book.book_num -=1
        book.save()

        return redirect(reverse("book_guan:reader_book",args=(id,)))
    else:
        return redirect(reverse("book_guan:reader_book",args=(id,)))
def reader_history(request):
    username = request.session.get("username")
    user1 = User.objects.get(username=username)
    histroys=user1.jieshu_lishi_set.all()
    print(type(histroys))
    return render(request,'reader_histroy.html',{"histroys":histroys})
def add_img(request):
    if request.method=="GET":
        return render(request,"add_img.html",{})
    elif request.method=='POST':
        name=request.POST['name']
        index=request.POST['index']
        pic=request.FILES['pic']
        img1=models.Img(index=index,name=name,pic=pic)
        img1.save()
        return redirect(reverse("book_guan:index"))
def add_blog(request):
    if request.method=="GET":
        return render(request,"add_blog.html",{})
    elif request.method=='POST':
        title = request.POST['title']
        massage = request.POST['massage']
        bolg1=models.Blog(title=title,massage=massage)
        bolg1.save()
        return redirect(reverse("book_guan:index"))

def active(request,strid):
    result = Serializer(settings.SECRET_KEY, 300)
    try:
        obj=result.loads(strid)
        user=models.User_file.objects.get(pk=obj['user_id']).user

        user.is_active=True
        user.save()
        return  redirect(reverse("book_guan:reader_login"))
    except SignatureExpired as e:
        return HttpResponse("连接失败")
def ajex_login(request):
    if request.method=="GET":
        return render(request, "ajex_login.html", {})
    elif request.method=='POST':
        return HttpResponse("登陆成功")
def checkuser(request):
    if request.method=='POST':
        username=request.POST["username"]
        user = authenticate(username=username)
        if user is not None:
            return HttpResponse("存在")
        else:
            return HttpResponse("不存在")