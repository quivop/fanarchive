"""
archive URL Configuration

"""
# from django.contrib import admin
from django.urls import path, include  # we need include, so add it here

urlpatterns = [
    # forward requests for root links to fanfic app
    path('', include('fanfic.urls', namespace='fanfic')),
]
