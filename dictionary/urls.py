from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('delete/<str:pk>', views.delete, name='delete'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('register/', views.registerView, name="register"),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
    path('welcome/', views.welcome, name='welcome'),
    path('', views.index, name='index'),
]
