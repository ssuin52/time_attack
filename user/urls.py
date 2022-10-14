
from django.urls import path, include
from . import views

urlpatterns = [
    path('signup/', views.sign_up_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout, name='logout'),
    path('home/', views.home_view, name='home'),
]