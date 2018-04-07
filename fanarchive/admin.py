from django.contrib import admin

# registering our models
from .models import Fic, FicPart

admin.site.register(Fic)
admin.site.register(FicPart)
