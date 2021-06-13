from django.contrib.auth import views
from ..forms import AuthenticationForm


class LoginView(views.LoginView):
    template_name = 'account/login.html'
    authentication_form = AuthenticationForm
