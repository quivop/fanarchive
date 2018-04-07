"""archive URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
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
    path('', RedirectView.as_view(url='/fanarchive/')),
]
