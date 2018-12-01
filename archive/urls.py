"""
archive URL Configuration

"""
# from django.contrib import admin
from django.urls import path, include  # we need include, so add it here

# Import RedirectView so redirecting our base url
# to the fanfic app will work
from django.views.generic import RedirectView

urlpatterns = [
    # path('admin/', admin.site.urls),

    # forward requests for 'archive/' links to urls.py
    # in the fanfic app
    path('', include('fanfic.urls', namespace='fanfic')),

    # redirect the base url to the fanfic app
    path('', RedirectView.as_view(url='archive/')),
]
