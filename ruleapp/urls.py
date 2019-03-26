from django.urls import path
from . import views

urlpatterns = [
    path('addrule/', views.addrule, name='addrule'),
    path('login/', views.user_login, name='login'),
    path('mail/', views.email),
]