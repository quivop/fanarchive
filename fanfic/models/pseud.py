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


class PseudGroup(models.Model):
    """
    Stores a single pseudonym group.
    """

    name = models.CharField('group name', max_length=100,
                            unique=True, blank=True)

    def __str__(self):
        """
        Human-readable representation of a :model:`pseud.PseudGroup`.
        """

        if self.name:
            return self.name
        else:
            return 'butts'
            # author_list = self.get_authors()
            # author_string = ', '.join(str(a) for a in author_list)

            # return author_string

    def get_authors(self):
        author_list = self.authors.all()
        return author_list


class PseudInstance(models.Model):
    """
    Stores a single instance of a Pseud joining a PseudGroup.
    """

    pseud = models.ForeignKey('Pseud', verbose_name='pseud',
                              on_delete=models.CASCADE)
    pseud_group = models.ForeignKey(
        'PseudGroup',
        on_delete=models.CASCADE)

    def __str__(self):
        """
        Human-readable representation of an Authorship
        """
        pseud = str(self.pseud)
        pseud_group = str(self.pseud_group)

        instance_desc = "{} joined pseud group {}".format(pseud, pseud_group)

        return instance_desc
