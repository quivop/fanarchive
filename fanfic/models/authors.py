from django.db import models


class AuthorGroup(models.Model):
    authors = models.ManyToManyField(
        'Pseud',
        through='Authorship',
    )

    # def __str__(self):
    #     """
    #     Human-readable representation of an AuthorGroup
    #     """
    #     author_list = self.get_author_list()

    #     list_length = len(author_list)

    def get_author_list(self):
        author_list = self.authors.all()
        return author_list


class Authorship(models.Model):
    author_group = models.ForeignKey(
        'AuthorGroup',
        on_delete=models.CASCADE)
    author = models.ForeignKey(
        'Pseud',
        on_delete=models.CASCADE)

#     def __str__(self):
#         """
#         Human-readable representation of an Authorship
#         """
#         return "{author} joined author \
# group %{author_group}" % (self.author,
#                           self.author_group)
