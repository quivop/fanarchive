from django.contrib import admin

# registering our models
from .models import Work, WorkPart

admin.site.register(Work)
admin.site.register(WorkPart)
