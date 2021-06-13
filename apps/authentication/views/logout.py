from django.contrib.auth import views


class LogoutView(views.LogoutView):
    next_page = '/'
