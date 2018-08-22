from django.conf import settings
from django.db import models


class Pseud(models.Model):
    """
    Stores a single pseudonym. Related to :model:`users.ArchiveUser`,
    :model:`authors.AuthorGroup` and :model:`authors.Authorship`.
    """

    pseud_name = models.CharField('pseud name', max_length=100)
    # needs enforcing @ db level
    pseud_owner = models.ForeignKey(
                                    settings.AUTH_USER_MODEL,
                                    on_delete=models.CASCADE)
