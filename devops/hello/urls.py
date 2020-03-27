#__author__ = 'richeng'

from django.urls import path

from . import views
urlpatterns = [
    # path('hello/', views.index, name='hello1'),
    path('hello/', views.index, name='hello2'),
    path('', views.index, name='index'), #If this pattern is targeted in an include(), ensure the include() pattern has a trailing '/'.
    # path('', views.index, name='index'),
]