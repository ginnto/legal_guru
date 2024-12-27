from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),   #urladdressname , function call, path name
    path('register',views.register,name='register')
]
