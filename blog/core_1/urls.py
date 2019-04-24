from django.conf.urls import url

from . import views

app_name='core_1'
urlpatterns = [
    url(r'^fenlei/(\d+)/$',views.fenlei,name='fenlei'),
    url(r'$',views.index,name='index'),

]