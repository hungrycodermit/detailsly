from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
       path('', views.index, name='index'),
       path('deleteoperation/<int:id>', views.delete_data, name='delete'),
       path('updateoperation/<int:id>', views.update_data, name='update'),
       path('signup', views.sign_up, name='signup'),
       path('login', views.login_process, name='login'),
       path('logout', views.logout_process, name='logout'),
       path('details', views.details_page, name='details'),
]
