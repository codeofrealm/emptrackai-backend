from django.urls import path

from .views import register_admin

urlpatterns = [
    path('register/', register_admin, name='register-admin'),
]