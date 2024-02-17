from django.urls import path

from auth_app import views

app_name = 'auth_app'

urlpatterns = [
    path('register/', views.register_request, name='register'),
    path('', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
    path('home/', views.home, name='home'),
]
