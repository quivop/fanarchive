from django.db import models


class AuthorGroup(models.Model):
    authors = models.ManyToManyField(
        'Pseud',
        through='Authorship',
    )

    def __str__(self):
        """
        Human-readable representation of an AuthorGroup
        """
        author_list = self.get_authors()
        author_string = ', '.join(str(a) for a in author_list)

        return author_string

    def get_authors(self):
        author_list = self.authors.all()
        return author_list


class Authorship(models.Model):
    author_group = models.ForeignKey(
        'AuthorGroup',
        on_delete=models.CASCADE)
    author = models.ForeignKey(
        'Pseud',
        on_delete=models.CASCADE)

    class Meta:
        unique_together = ("author_group", "author")

    def __str__(self):
        """
        Human-readable representation of an Authorship
        """
        author = str(self.author)
        author_group = str(self.author_group)

        authorship = "{} joined author group {}".format(author, author_group)

        return authorship
