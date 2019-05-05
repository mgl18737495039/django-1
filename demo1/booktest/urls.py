from django.conf.urls import url

from . import views
app_name='booktest'
urlpatterns = [
    url('index/$',views.index,name='index'),
    url('list/$',views.list,name='list'),
    url(r'^xiang/(\d+)/$',views.xiang,name='xiang'),
    url(r'dele/(\d+)$',views.dele,name='dele')
]