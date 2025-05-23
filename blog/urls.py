from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<slug:slug>/', views.detail, name='detail'),
    path('create/', views.create_post, name='create'),
]