"""djangoProject001 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from django.shortcuts import HttpResponse, render
from app01 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login),
    path('', views.index),
    path('index/', views.index),
    path('main/', views.main),
    path('try_login/', views.try_login),
    re_path(r'^delete_(press|book|author)/(\d+)/$', views.delete),
    # day60--------------------------
    path('press_list/', views.press_list, name='press'),
    # path('add_press/', views.add_press),
    path('add_press/', views.AddPress.as_view()),
    # path('delete_press/', views.delete_press),
    path('edit_press/', views.edit_press),
    path('edit_press2/', views.edit_press2),
     # day61--------------------------
    path('book_list/', views.book_list, name='book'),
    path('add_book/', views.add_book),
    # path('delete_book/', views.delete_book),
    path('edit_book/', views.edit_book),
    # day62--------------------------
    path('author_list/', views.author_list, name='author'),
    path('add_author/', views.add_author),
    # path('delete_author/', views.delete_author),
    path('edit_author/', views.edit_author),
    path('upload/', views.upload),


]
