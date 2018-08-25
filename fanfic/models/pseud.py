from django.conf import settings
from django.db import models
from django.utils import timezone


class Pseud(models.Model):
    """
    Stores a single pseudonym. Related to :model:`users.ArchiveUser`,
    :model:`authors.AuthorGroup` and :model:`authors.Authorship`.
    """

    pseud_name = models.CharField('pseud name', max_length=100,
                                  unique=True)
    # needs enforcing @ db level
    pseud_owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                                    on_delete=models.CASCADE)

    date_created = models.DateTimeField('date created',
                                        default=timezone.now)

    def __str__(self):
        """
        Human-readable representation of a :model:`pseud.Pseud`.
        """
        return self.pseud_name
