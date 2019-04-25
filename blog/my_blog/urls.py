from django.conf.urls import url

from . import views

app_name='my_blog'
urlpatterns = [
    url(r'^my_blog/',views.my_blog,name='my_blog'),
    url(r'^send_blog/',views.send_blog,name='send_blog'),
    url(r'^del_blog/(\d+)/$',views.del_blog,name='del_blog'),
    url(r'^xiugai_user/$',views.xiugai_user,name='xiugai_user'),
    url(r'^my_blogcoll/',views.my_blogcoll,name='my_blogcoll'),



]