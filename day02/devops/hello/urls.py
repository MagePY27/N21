#__author__ = 'richeng'

from django.urls import path,re_path
from . import views,views1
from . import views

app_name = 'hello'
urlpatterns = [
    path('', views.index, name='index'), #If this pattern is targeted in an include(), ensure the include() pattern has a trailing '/'.
    path('useradd/', views1.useradd, name='useradd'),
    path('userlist/', views1.userlist, name='userlist'),
    re_path('modify/(?P<pk>[0-9]+)?/', views1.modify, name='modify'),
    re_path('userdel/(?P<pk>[0-9]+)?/', views1.userdel, name='userdel'),
]