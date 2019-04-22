from django.conf.urls import url

from . import views

app_name='my_blog'
urlpatterns = [
    url(r'^my_blog/',views.my_blog,name='my_blog'),
    url(r'^send_blog/',views.send_blog,name='send_blog'),

]