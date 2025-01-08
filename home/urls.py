from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),   #urladdressname , function call, path name
    path('logout',views.logout,name='logout'),
    path('chats/', views.chat_list, name='chat_list'),
    # path('chats/<int:chat_id>/', views.chat_detail, name='chat_detail'),
    path('send_message/<int:id>/', views.send_message, name='send_message'),

]
