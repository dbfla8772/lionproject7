from django.core import mail
from django.urls import path
from .views import *   

app_name = 'mail'

urlpatterns = [   
    path('',send_mail, name="mail"),  
]