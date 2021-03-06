from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# class User(models.Model):
#     username=models.CharField(max_length=20)
#     password=models.CharField(max_length=20)
#
#
#
#
#     def __str__(self):
#         return self.username
class User_file(models.Model):

    age=models.IntegerField(default=0)
    nickname=models.CharField(max_length=50)
    gender=models.CharField(max_length=5,default='xxx')
    pthone=models.CharField(max_length=30,default='xxxxx')
    hobby_user=models.TextField(default='无')
    speciality=models.TextField(default='无')
    Personal_quotes=models.TextField(default='无')
    user_img=models.FileField(upload_to='./static/images/users/',default='static/images/users/user.jpg')
    user_file = models.OneToOneField(User, on_delete=models.CASCADE)
    def sex1(self):
        return self.sex
    sex1.short_description = '性别'

    def __str__(self):
        return self.username
class Article(models.Model):
    article_name=models.CharField(max_length=40)
    article_time=models.DateTimeField(auto_now_add=True)
    article_user=models.ForeignKey(User,on_delete=models.CASCADE)
    article_text=models.TextField()
    article_click_volume=models.IntegerField(default=0)
    article_img=models.FileField(upload_to='./static/images/')
    article_category=models.ForeignKey('Sort',on_delete=models.CASCADE)
    article_num=models.IntegerField(default=0)

    def __str__(self):
        return self.article_name
class Comment(models.Model):
    comment_article=models.ForeignKey("Article",on_delete=models.CASCADE)
    comment_user=models.ForeignKey(User,on_delete=models.CASCADE)
    comment_text=models.TextField()
    comment_time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_text
class Sort(models.Model):
    sort_name=models.CharField(max_length=40)
    def __str__(self):
        return self.sort_name
class Collection(models.Model):
    collection_article=models.ForeignKey("Article",on_delete=models.CASCADE)
    collection_user=models.ForeignKey(User,on_delete=models.CASCADE)
    collection_time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self. collection_time