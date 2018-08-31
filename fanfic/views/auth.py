from fanfic.forms import LoginForm
from authtools.views import LoginView as AuthToolsLoginView


class MyLoginView(AuthToolsLoginView):
    template_name = 'auth/login.html'
    authentication_form = LoginForm()
