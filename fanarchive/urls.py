from django.urls import path

from . import views

app_name = 'fanarchive'
urlpatterns = [
    # pointing to dynamic index view
    path('', views.IndexView.as_view(), name='index'),
    # pointing to /fanarchive/5/
    path('fic/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('test/', views.TestView.as_view(), name='test'),
    path('admin/edit/', views.FicEditingView, name='fic-editing-view'),
]
