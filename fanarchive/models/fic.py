from django.db import models
from datetime import date


class Fic(models.Model):
    fic_title = models.CharField('fic title', max_length=200)
    # remember, this is enforced only at view level, not on db or in the model. needs testing
    fic_summary = models.TextField('fic summary', max_length=500)
    # default to today
    date_created = models.DateField('date created', default=date.today)

    def __str__(self):
        # returns title of the Fic when called by __str__() method
        return self.fic_title
