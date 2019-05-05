from django.conf.urls import url

from . import views
app_name='book_guan'
urlpatterns = [

    url(r'^index/$', views.index,name="index"),
    url(r'^reader_login/$',views.reader_login,name="reader_login"),
    url(r'^register/$',views.register,name="register"),
    url(r'^reader/$',views.reader,name="reader"),
url(r'^user_logout/$',views.user_logout,name="user_logout"),
url(r'^reader_info/$',views.reader_info,name="reader_info"),
url(r'^reader_modify/$',views.reader_modify,name="reader_modify"),
url(r'^reader_query/$',views.reader_query,name="reader_query"),
url(r'^reader_book/(\d+)/$',views.reader_book,name="reader_book"),
url(r'^jie/(\d+)/$',views.jie,name="jie"),
url(r'^reader_history/$',views.reader_history,name="reader_history"),
url(r'^add_img/$',views.add_img,name="add_img"),
url(r'^add_blog/$',views.add_blog,name="add_blog"),
url(r'^active/(.*?)/$',views.active,name="active"),
    url(r'^ajex_login/$', views.ajex_login, name="ajex_login"),
url(r'^checkuser/$', views.checkuser, name="checkuser"),



]