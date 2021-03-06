from django.urls import path

from . import views


app_name = 'fanfic'
urlpatterns = [
    # pointing to dynamic index view
    path('', views.IndexView.as_view(), name='index'),
    # pointing to /fic/5/
    path('fic/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('test/', views.TestView.as_view(), name='test'),
    # path('admin/<int:pk>/edit/', views.FicEditingView, name='fic-editing-view'),
    path('panel/', views.MyPanel.as_view(), name='panel'),
    path('panel/new/fic/', views.TestView.as_view(), name='newfic')
]
