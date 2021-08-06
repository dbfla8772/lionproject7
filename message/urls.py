from django.urls import path
from .views import *   

urlpatterns = [   
    path('inbox/', inbox, name="inbox"),
    path('send_box/', send_box, name="send_box"),
    path('<str:id>', detail_message, name="detail_message"),  
    path('new/', new_message, name="new_message"),
]