from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.handlelogin, name='handlelogin'),
    path('logout/', views.handlelogout, name='handlelogout'),
    path('contact/', views.contact, name='contact'),
    path('join/', views.enroll, name='enroll'),
]
