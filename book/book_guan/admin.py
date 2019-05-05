from django.contrib import admin

# Register your models here.
from . import models
from django.contrib.auth.models import User
# Register your models here.

class User_fileAdmin(admin.ModelAdmin):
    # list_display：显示字段，可以点击列头进行排序
    list_display = ['id',"user_college","user_num_stu","user"]
    # list_filter：过滤字段，过滤框会出现在右侧
    list_filter = ['user_num_stu']
    # search_fields：搜索字段，搜索框会出现在上侧
    search_fields = ['user_num_stu']
class Book_infoAdmin(admin.ModelAdmin):
    list_display = ['id',"book_name","book_banshe","book_author","book_num","publish_date"]
    list_filter = ['book_name']
    # search_fields：搜索字段，搜索框会出现在上侧
    search_fields = ['book_name']
class JieshuAdmin(admin.ModelAdmin):
    list_display = ['id',"book","user","jie_chu","huan_book"]
    list_filter = ['jie_chu']
    # search_fields：搜索字段，搜索框会出现在上侧
    search_fields = ['jie_chu']
class Jieshu_lishiAdmin(admin.ModelAdmin):
    list_display = ['id',"book","user","jie_chu","huan_book"]
    list_filter = ['jie_chu']
    # search_fields：搜索字段，搜索框会出现在上侧
    search_fields = ['jie_chu']

admin.site.register(models.Book_info,Book_infoAdmin)
admin.site.register(models.User_file,User_fileAdmin)
admin.site.register(models.Jieshu,JieshuAdmin)
admin.site.register(models.Jieshu_lishi,Jieshu_lishiAdmin)
admin.site.register(models.Img)
admin.site.register(models.Blog)



