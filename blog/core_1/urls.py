from django.conf.urls import url

from . import views

app_name='core_1'
urlpatterns = [
    url(r'$',views.index,name='index'),

]