from django.urls import path

from .views import *

urlpatterns = [
    # Dashboard URL
    path('', DashboardView.as_view(), name='dashboard'),
]
