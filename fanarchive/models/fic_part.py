from django.db import models


class FicPart(models.Model):
    fic_part_title = models.CharField('fic part title', max_length=200)
    fic_part_text = models.TextField('fic part text')

    # One FicPart can have many Fics, but a FicPart can only have one Fic
    fic = models.ForeignKey('Fic', on_delete=models.CASCADE)

    # FicParts have part numbers
    fic_part_number = models.PositiveIntegerField()

    def __str__(self):
        # returns title of the FicPart when called by __str__()
        return self.fic_part_title
