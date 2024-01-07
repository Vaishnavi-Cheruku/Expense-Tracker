from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('register/',views.register,name='register'),
    path('handleSignup/',views.handleSignup,name='handleSignup'),
    path('handlelogin/',views.handlelogin,name='handlelogin'),
     path('handleLogout/',views.handleLogout,name='handleLogout'),
     path('reset_password/',auth_views.PasswordResetView.as_view(template_name = "home/reset_password.html"),name='reset_password'),
     path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name="home/reset_password_sent.html"),name='password_reset_done'),
     path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name ="home/password_reset_form.html"),name='password_reset_confirm'),
     path('reset_password_complete/',auth_views.PasswordResetView.as_view(template_name ="home/password_reset_done.html"),name='password_reset_complete'),
     path('addmoney/',views.addmoney,name='addmoney'),
    path('charts/',views.charts,name='charts'),
     path('tables/',views.tables,name='tables'),
     path('expense_edit/<int:id>',views.expense_edit,name='expense_edit'),
     path('profile/',views.profile,name = 'profile'),
     path('stats/',views.stats, name = 'stats'),
     path('weekly/',views.weekly, name = 'weekly'),
    path('info/',views.info,name="info"),
]
