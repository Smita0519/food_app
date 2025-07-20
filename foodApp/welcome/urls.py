from django.urls import path, include
from . import views

app_name = 'welcome'
urlpatterns = [
    path('', views.welcomePage, name='welcomePage'),    
]