
from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

class User_file(models.Model):
    user_college=models.CharField(max_length=40,default='无')
    user_num_stu=models.CharField(max_length=20,default='000000')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.user_num_stu
class Book_info(models.Model):
    book_name=models.CharField(max_length=100)
    book_banshe=models.CharField(max_length=100)
    book_author=models.CharField(max_length=100)
    book_num=models.IntegerField(default=100)
    publish_date=models.CharField(max_length=100)
    def __str__(self):
        return self.book_name
class Jieshu(models.Model):
    book=models.ForeignKey('Book_info',on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    jie_chu=models.DateTimeField(auto_now_add=True)
    huan_book=models.DateTimeField()
    def __str__(self):
        return self.jie_chu
class Jieshu_lishi(models.Model):
    book=models.ForeignKey('Book_info',on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    jie_chu=models.DateTimeField(auto_now_add=True)
    huan_book=models.DateTimeField()
    def __str__(self):
        return self.jie_chu
class Img(models.Model):
    name=models.CharField(max_length=100)
    pic=models.ImageField(upload_to='hotpic')
    index=models.SmallIntegerField()
    def __str__(self):
        return self.name
class Blog(models.Model):
    title=models.CharField(max_length=20)
    massage=HTMLField()
    def __str__(self):
        return self.title
