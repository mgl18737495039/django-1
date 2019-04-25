from django.conf.urls import url

from . import views
app_name='blog_1'
urlpatterns = [

    url(r'^register/', views.register,name='register'),
    url(r'^login/',views.user_login,name='user_login'),
    url(r'^logout/',views.user_logout,name='user_logout'),
    url(r'^update_pwd/',views.update_pwd,name='update_pwd'),
]