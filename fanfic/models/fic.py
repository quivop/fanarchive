from django.db import models
from django.utils import timezone


class Fic(models.Model):
    fic_title = models.CharField('fic title', max_length=200)
    # remember, this is enforced only at view level, not on db or in the model. needs testing
    fic_summary = models.TextField('fic summary', max_length=500)
    # default both date fields to now
    pub_date = models.DateTimeField('date published', default=timezone.now)
    date_updated = models.DateTimeField('date updated', default=timezone.now)
    fic_author_group = models.ForeignKey('AuthorGroup', on_delete=models.CASCADE)

    def __str__(self):
        """
        String for representing the Model object
        """
        return self.fic_title

    def get_absolute_url(self):
        """
        Returns the url to access the detail page for this fanfic
        """
        from django.urls import reverse
        return reverse('fanfic:detail', args=[str(self.id)])

    def get_fic_authors(self):
        """
        Returns a list of the fic author(s)
        """
        pass
