from django.urls import path
from . import views

urlpatterns = [
    path('ticket-status/', views.ticket_status),
    path('send-status/', views.send_status),
]