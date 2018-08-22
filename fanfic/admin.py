from django.contrib import admin

# registering our models
from .models import Fic, FicPart, AuthorGroup, Authorship, Pseud

admin.site.register(Fic)
admin.site.register(FicPart)
admin.site.register(AuthorGroup)
admin.site.register(Authorship)
admin.site.register(Pseud)
