from django.db import models
from datetime import date


class Work(models.Model):
    work_title = models.CharField('work title', max_length=200)
    # remember, this is enforced only at view level, not on db or in the model. needs testing
    work_summary = models.TextField('work summary', max_length=500)
    # default to today
    date_created = models.DateField('date created', default=date.today)

    def __str__(self):
        # returns title of the Work when called by __str__() method
        return self.work_title
