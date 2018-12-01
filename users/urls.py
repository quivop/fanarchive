from django.urls import path, include
from authtools.views import LoginView as AuthToolsLoginView
from django.views.generic import RedirectView

urlpatterns = [
    path('login/', AuthToolsLoginView.as_view(template_name='users/login.html'), name='login'),
    path('', RedirectView.as_view(url='login/'))
]
