from django.db import models


class AuthorGroup(models.Model):
    authors = models.ManyToManyField(
        'Pseud',
        through='Authorship',
    )


class Authorship(models.Model):
    author_group = models.ForeignKey(
        'AuthorGroup',
        on_delete=models.CASCADE)
    author = models.ForeignKey(
        'Pseud',
        on_delete=models.CASCADE)
