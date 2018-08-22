from django.db import models
from django.utils import timezone


class Fic(models.Model):
    """
    Stores a single fanfic, related to :model:`fic_part.FicPart`
    and :model:`authors.AuthorGroup`.
    """

    # max_length only enforced at view level
    fic_title = models.CharField('fic title', max_length=200)
    fic_summary = models.TextField('fic summary', max_length=500)

    # default both date fields to now
    pub_date = models.DateTimeField('date published', default=timezone.now)
    date_updated = models.DateTimeField('date updated', auto_now=True)

    fic_author_group = models.ForeignKey(
        'AuthorGroup', on_delete=models.CASCADE,
        verbose_name='fic author(s)')

    def __str__(self):
        """
        Human-readable representation of a :model:`fic.Fic`
        """
        return self.fic_title

    def get_absolute_url(self):
        """
        Returns the url to access the detail page for a Fic.
        """
        from django.urls import reverse
        return reverse('fanfic:detail', args=[str(self.id)])

    def get_fic_authors(self):
        """
        Returns an alphabetized list of the fic author(s) for a Fic.
        """
        pass
