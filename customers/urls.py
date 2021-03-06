from django.urls import path
from . import views

app_name = 'customers'

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('profile', views.profile, name='profile'),
    path('history', views.history, name='history'),
    path('send-money', views.send, name='send_money')
]