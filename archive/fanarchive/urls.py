from django.urls import path

from . import views

app_name = 'fanarchive'
urlpatterns = [
	# pointing to super-simple index view
	path('', views.index, name='index'),
	# pointing to /fanarchive/5/
	path('<int:work_id>/', views.detail, name='detail'),
	# pointing to /fanarchive/5/whole_work/
	path('<int:work_id>/whole_work/', views.whole_work, name="whole work"),
]