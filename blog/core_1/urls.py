from django.conf.urls import url

from . import views

app_name='core_1'
urlpatterns = [
    url(r'^fenlei/(\d+)/$',views.fenlei,name='fenlei'),
url(r'^hort_blog/$',views.hort_blog,name='hort_blog'),
url(r'^new_blog/$',views.new_blog,name='new_blog'),
url(r'^com_blog/$',views.com_blog,name='com_blog'),
url(r'^find/$',views.find,name='find'),
url(r'^coll_blog/(\d+)/$',views.coll_blog,name='coll_blog'),
url(r'$',views.index,name='index'),

]