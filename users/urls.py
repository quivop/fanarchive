from django.urls import path, include, reverse_lazy
from authtools.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from . import views

from django.views.generic import RedirectView

app_name = "users"
urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('', RedirectView.as_view(url='login/')),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('password_reset/', views.ResetView.as_view(), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),

    # routes with un-implemented templates below here
    path('password_change/', PasswordChangeView.as_view(template_name='users/password_change.html'), name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'), name='password_change_done'),
    
    
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
]
