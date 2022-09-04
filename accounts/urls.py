from django.urls import path
from . import views

urlpatterns=[
    path('register',views.register,name='register'),
    path('log',views.log_gin,name='log'),
]
