from django.db import models

# Create your models here.

class Wen(models.Model):
    wen_name=models.CharField(max_length=100)
class Choice_wen(models.Model):
    choice_name=models.CharField(max_length=100)
    choice_num=models.IntegerField(default=0)
    wen_choice=models.ForeignKey('Wen',on_delete=models.CASCADE)