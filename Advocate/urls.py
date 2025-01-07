from django.urls import path
from . import views

urlpatterns = [

    path('advregister',views.advregister,name='advregister'),
    path('advlogin',views.advlogin,name='advlogin'),
    path('advdash',views.advdash,name='advdash'),
    path('advprofile',views.advprofile,name='advprofile'),
    path('advlogout',views.advlogout,name='advlogout'),
    path('case_list',views.case_list,name='case_list'),
    path('advpaymentlist,<int:id>',views.advpaymentlist,name='advpaymentlist'),
    path('current_case_list',views.current_case_list,name='current_case_list'),
]