from django.db import models

class AuthorGroup(models.Model):
    authors = models.ManyToManyField(
        'pseuds.Pseud',
        through='Authorship',
    )


class Authorship(models.Model):
    author_group = models.ForeignKey(
        'AuthorGroup',
        on_delete=models.CASCADE)
    author = models.ForeignKey(
        'pseuds.Pseud',
        on_delete=models.CASCADE)