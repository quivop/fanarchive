from django.db import models
from datetime import date
from django.utils import timezone


class Fic(models.Model):
    fic_title = models.CharField('fic title', max_length=200)
    # remember, this is enforced only at view level, not on db or in the model. needs testing
    fic_summary = models.TextField('fic summary', max_length=500)
    # default both date fields to now
    pub_date = models.DateTimeField('date published', default=timezone.now)
    date_updated = models.DateTimeField('date updated', default=timezone.now)

    def __str__(self):
        # returns title of the Fic when called by __str__() method
        return self.fic_title
