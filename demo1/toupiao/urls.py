from django.conf.urls import url

from . import views
app_name='toupiao'
urlpatterns = [
    url(r'^toupiao/$',views.toupiao,name='toupiao'),
    url(r'^dell/(\d+)/$',views.dell,name='dell'),
    url(r"^xiangqing/(\d+)/$", views.xiangqing, name='xiangqing'),
    url(r"^add_piao/(\d+)/$", views.add_piao, name='add_piao'),
    url(r"^add_choice/(\d+)/$", views.add_choice, name='add_choice'),
    url(r'^.*$',views.add_wen,name='add_wen'),

    ]