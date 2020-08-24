from django.urls import path

from . import views

urlpatterns = [
    path('', views.allblogs, name='allblogs'), #request from main folder urls.py to main
    path('<int:blog_id>/', views.detail, name='detail') #request from main folder urls.py to detail;
    # after/blog/ an integer is considered as id
]