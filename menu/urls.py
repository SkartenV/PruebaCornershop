from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    #url(r'^$', views.Add_Menu, name='Add_Menu'),
    #path('add', views.Add_Menu),
    url('add', views.Add_Menu, name='add_menu'),
    url('', views.CantidadMenu, name='home'),

]