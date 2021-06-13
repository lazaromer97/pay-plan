from django.contrib.auth import views


class PasswordChangeDoneView(views.PasswordChangeDoneView):
    template_name = 'account/password_change_done.html'
    title = ('Contraseña Cambiada Correctamente')
