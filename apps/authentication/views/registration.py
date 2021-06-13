from django.views import generic
from django.urls import reverse_lazy

from ..forms import RegistrationForm


class RegistrationView(generic.CreateView):
    form_class = RegistrationForm
    template_name = 'account/signup.html'
    success_url = reverse_lazy('login')
