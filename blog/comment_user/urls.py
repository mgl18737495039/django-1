from django.conf.urls import url

from . import views
app_name='comment_user'
urlpatterns = [

    url(r'^comment_user/(\d+)/$', views.comment_user,name='comment_user'),
    url(r'^user_side/(\d+)/$', views.user_side,name='user_side'),

]