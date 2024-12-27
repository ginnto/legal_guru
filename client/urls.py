from django.urls import path
from . import views

urlpatterns = [
    path('clientdash',views.clientdash,name='clientdash'),
    path('clientregister',views.clientregister,name='clientregister'),
]