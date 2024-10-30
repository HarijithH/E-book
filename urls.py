from django.contrib import admin
from django.urls import path

from Ebook_app import views

urlpatterns = {
    path('', views.login, name="login"),
    path('user_feedback', views.user_feedback, name="user_feedback"),
    path('view_complaint', views.view_complaint, name="view_complaint"),
    path('send_reply', views.send_reply, name="send_reply"),
    path('view_history', views.view_history, name="view_history"),
    path('admin_home', views.admin_home, name="admin_home"),


}
