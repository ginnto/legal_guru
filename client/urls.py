from django.urls import path
from . import views

urlpatterns = [
    path('clientdash',views.clientdash,name='clientdash'),
    path('clientlogin',views.clientlogin,name='clientlogin'),
    path('clientcase',views.clientcase,name='clientcase'),
    path('clientprofile',views.clientprofile,name='clientprofile'),
    path('clientcaselist',views.clientcaselist,name='clientcaselist'),
    path('clientregister',views.clientregister,name='clientregister'),
    path('submit_feedback/', views.submit_feedback, name='submit_feedback'),
    path('feedback_list/', views.feedback_list, name='feedback_list'),

]