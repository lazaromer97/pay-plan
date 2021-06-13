from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from ..models import PaymentPlan

from ..forms import PaymentPlanForm

# Create your views here.


class PaymentPlanListView(ListView):
    model = PaymentPlan
    template_name = 'payment_plan/index.html'
    context_object_name = 'payment_plans'
    queryset = PaymentPlan.objects.all()


class PaymentPlanCreateView(CreateView):
    model = PaymentPlan
    template_name = 'payment_plan/create.html'
    form_class = PaymentPlanForm
    success_url = reverse_lazy('payment_plan_list')


class PaymentPlanUpdateView(UpdateView):
    model = PaymentPlan
    template_name = 'payment_plan/update.html'
    form_class = PaymentPlanForm
    success_url = reverse_lazy('payment_plan_list')


class PaymentPlanDeleteView(DeleteView):
    model = PaymentPlan
    template_name = 'payment_plan/delete.html'
    success_url = reverse_lazy('payment_plan_list')
