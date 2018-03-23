from django.urls import path

from . import views

app_name = 'fanarchive'
urlpatterns = [
	# pointing to super-simple index view
	path('', views.IndexView.as_view(), name='index'),
	# pointing to /fanarchive/5/
	path('<int:pk>/', views.DetailView.as_view(), name='detail')
]