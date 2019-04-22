from django.contrib import admin
from . import models
from django.contrib.auth.models import User
# Register your models here.

class User_fileAdmin(admin.ModelAdmin):
    # list_display：显示字段，可以点击列头进行排序
    list_display = ['id',"age","gender","hobby_user","speciality","user_file",'pthone','nickname']
    # list_filter：过滤字段，过滤框会出现在右侧
    list_filter = ['pthone']
    # search_fields：搜索字段，搜索框会出现在上侧
    search_fields = ['pthone']

    # list_per_page：分页，分页框会出现在下侧
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id','article_name',"article_time","article_user","article_text","article_click_volume","article_img","article_category"]

    list_filter = ['article_name']
    # search_fields：搜索字段，搜索框会出现在上侧
    search_fields = ['article_name']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['id','comment_article','comment_user',"comment_text","comment_time"]
    list_filter = ['comment_text']
    # search_fields：搜索字段，搜索框会出现在上侧
    search_fields = ['comment_text']

admin.site.register(models.User_file,User_fileAdmin)
admin.site.register(models.Comment,CommentAdmin)
admin.site.register(models.Article,ArticleAdmin)