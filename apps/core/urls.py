from django.urls import path

from .views import *

urlpatterns = [
    # Dashboard URL
    path('', DashboardView.as_view(), name='dashboard'),

    # Payment Plan
    path('payment_plan/', PaymentPlanListView.as_view(), name='payment_plan_list'),
    path('payment_plan/create/', PaymentPlanCreateView.as_view(), name='payment_plan_create'),
    path('payment_plan/update/<int:pk>/', PaymentPlanUpdateView.as_view(), name='payment_plan_update'),
    path('payment_plan/delete/<int:pk>/', PaymentPlanDeleteView.as_view(), name='payment_plan_delete'),
]
