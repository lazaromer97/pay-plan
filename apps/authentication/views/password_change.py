from django.urls import reverse_lazy
from django.contrib.auth import views
from ..forms import PasswordChangeForm


class PasswordChangeView(views.PasswordChangeView):
    template_name = 'account/password_change_form.html'
    success_url = reverse_lazy('password_change_done')
    form_class = PasswordChangeForm
    title = ('Cambiar Contraseña')
