from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),   #urladdressname , function call, path name
    path('logout',views.logout,name='logout'),
    path('chats/', views.chat_list, name='chat_list'),
    path('advchats/', views.advchat_list, name='advchat_list'),
    path('send_message/<int:id>/', views.send_message, name='send_message'),

]
