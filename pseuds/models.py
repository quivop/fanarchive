from django.conf import settings
from django.db import models

# Pseudonyms ahoy!


class Pseud(models.Model):
    pseud_name = models.CharField('pseud name', max_length=100)
    # needs enforcing @ db level
    pseud_owner = models.ForeignKey('pseud owner',
                                    settings.AUTH_USER_MODEL,
                                    on_delete=models.CASCADE)
