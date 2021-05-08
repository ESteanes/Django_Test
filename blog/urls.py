from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='blog_home'),
    path('Account/', views.account, name='blog_account'),
    path('About/', views.about, name='blog_about')
]