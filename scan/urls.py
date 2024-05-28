# scan/urls.py
from django.urls import path
from .views import scan_view, index

urlpatterns = [
    path('', index, name='home'),
    path('scan/', scan_view, name='scan'),
]
