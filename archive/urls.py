"""
archive URL Configuration

"""
from django.contrib import admin
from django.urls import path, include  # we need include, so add it here

# Import RedirectView so redirecting our base url
# to the fanarchive app will work
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),

    # forward requests for 'fanarchive/' links to urls.py
    # in the fanarchive app
    path('fanarchive/', include('fanarchive.urls')),

    # redirect the base url to the fanarchive app
    path('', RedirectView.as_view(url='fanarchive/')),
]
