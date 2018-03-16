from django.urls import path

from . import views

urlpatterns = [
	# pointing to super-simple index view
	path('', views.index, name='index'),
]