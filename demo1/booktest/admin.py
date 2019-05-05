from django.contrib import admin
from .models import *
# Register your models here.

"""修改admin后台模块管理界面"""
# Register your models here.
class HeroInfoInline(admin.StackedInline):
    model =HeroInfo
    extra = 1
class BookInfoAdmin(admin.ModelAdmin):
    # list_display：显示字段，可以点击列头进行排序
    list_display = ['id', 'booktitle', 'book_time']
    # list_filter：过滤字段，过滤框会出现在右侧
    list_filter = ['booktitle']
    # search_fields：搜索字段，搜索框会出现在上侧
    search_fields = ['booktitle']
    # list_per_page：分页，分页框会出现在下侧
    list_per_page = 2
    inlines = [HeroInfoInline]
class HeroInfoAdmin(admin.ModelAdmin):
    # list_display：显示字段，可以点击列头进行排序
    list_display = ['id', 'hname', 'hgemder',"hcontent","hbook"]
    # list_filter：过滤字段，过滤框会出现在右侧
    list_filter = ['hname']
    # search_fields：搜索字段，搜索框会出现在上侧
    search_fields = ['hname']
    # list_per_page：分页，分页框会出现在下侧
    list_per_page = 2

admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo,HeroInfoAdmin)