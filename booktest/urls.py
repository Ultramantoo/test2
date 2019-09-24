from django.urls import re_path, path
from booktest import views

urlpatterns = [
    path('', views.index),
    path('index/', views.index),
    re_path(r'^delete(\d+)/$', views.delete),
    re_path(r'^create/$', views.create),
]
