from django.db import models

# Create your models here.


"""数据库表的模板"""
class BookInfo(models.Model):
    booktitle=models.CharField(max_length=20)
    book_time=models.DateTimeField(auto_now_add=True)
class HeroInfo (models.Model):
    hname=models.CharField(max_length=20)
    hgemder=models.BooleanField()
    hcontent=models.CharField(max_length=50)
    hbook=models.ForeignKey('BookInfo',on_delete=models.CASCADE)