from django.urls import path

from . import views

urlpatterns = [
	# pointing to super-simple index view
	path('', views.index, name='index'),
	# pointing to /fanarchive/5/
	path('<int:work_id>/', views.detail, name='detail'),
	# pointing to /fanarchive/5/whole_work/
	# path() will go here
]