from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    #url(r'^$', views.Add_Menu, name='Add_Menu'),
    #path('add', views.Add_Menu),
    #url('', views.CantidadMenu, name='inicio'),
    url('add', views.Add_Menu, name='add_menu'),
    #url('edit', views.Edit_Menu, name='edit_menu'),
    url('list', views.MenuListView.as_view(), name='see_menu'),
    #url(r'^edit/(?P<pk>\d+)$', views.Edit_Menu, name='edit_menu'),
    path('edit/<int:menu_id>', views.Edit_Menu, name='edit_menu'),
    #url(r'^menus/$', views.MenuListView.as_view(), name='menus'),
    #url(r'^menus/(?P<pk>\d+)$', views.MenuDetailView.as_view(), name='menu-detail'),

]