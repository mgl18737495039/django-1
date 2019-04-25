from django.shortcuts import render,redirect,reverse
from django.http import HttpResponseRedirect
from blog_1 import models
from django.contrib.auth.models import User
# Create your views here.
def comment_user(request,id):
    i=models.Article.objects.get(pk=id)
    i.article_click_volume +=1
    i.save()
    username = request.session.get("username")
    comments=i.comment_set.all()
    sorts = models.Sort.objects.all()
    return render(request,'comment_user.html',{"i":i,'username':username,'comments':comments,'sorts':sorts})
def user_side(request,id):
    username = request.session.get("username")
    comment_nei=request.POST['comment_nei']
    user1=User.objects.get(username=username)
    article= models.Article.objects.get(pk=id)
    article.article_num +=1
    comment1=models.Comment()
    comment1.comment_user=user1
    comment1.comment_article=article
    comment1.comment_text=comment_nei

    if comment_nei.isspace():
        return redirect(reverse('comment_user:comment_user',args=(id,)),{"erro_massage":"评论不能为空"})
        # return redirect('/')
        # # return redirect('/comment_user/comment_user.html')
    else:
        comment1.save()
        article.save()
        return redirect(reverse('comment_user:comment_user', args=(id,)))
