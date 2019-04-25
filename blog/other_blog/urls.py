from django.conf.urls import url

from static.css import views

app_name='other_blog'
urlpatterns = [
    url(r'^other_blog/(\d+)/', views.other_blog, name='other_blog'),



]