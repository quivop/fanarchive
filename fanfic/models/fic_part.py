from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone


class FicPart(models.Model):
    """
    Stores a single fic part (chapter, snippet, etc).
    Related to :model:`fic.Fic`.
    """

    fic_part_title = models.CharField(
        'fic part title', max_length=200)
    fic_part_text = models.TextField('fic part text')

    # One FicPart can have many Fics, but a FicPart can only have one Fic
    fic = models.ForeignKey('Fic', on_delete=models.CASCADE,
                            verbose_name='fic')

    pub_date = models.DateTimeField('date published', default=timezone.now)
    date_updated = models.DateTimeField('date updated', auto_now=True)

    # FicParts have part numbers
    fic_part_number = models.PositiveIntegerField(
        'fic part number', null=True)

    def __str__(self):
        """
        Human-readable representation of a :model:`fic_part.FicPart`.
        """
        return self.fic_part_title

    def Meta(self):
        unique_together = ("fic", "fic_part_number") # noqa

    def save(self, *args, **kwargs):
        """
        Custom save function for FicParts. Automatically assigns a
        fic_part_number to a new or updated FicPart as needed.
        """
        if self.fic_part_number is None:
            fic_part_number = calc_fic_part_number(
                fic_id=self.fic)
        else:
            fic_part_number = calc_fic_part_number(
                fic_part=self, fic_id=self.fic,
                fic_part_number=self.fic_part_number)
        self.fic_part_number = fic_part_number

        try:
            self.full_clean()
        except ValidationError as e:
            self.fic_part_number = None
            self.fic_part_number = calc_fic_part_number(
                fic_id=self.fic)
        else:
            super(FicPart, self).save(*args, **kwargs)


# FicPart utility functions

def calc_fic_part_number(fic_id, fic_part=None,
                         fic_part_number=None):
    """
    Calculates a fic_part_number for a new or updated FicPart.
    """

    # grab existing fic part numbers for the Fic of this FicPart
    existing_part_numbers = FicPart.objects.filter(
        fic=fic_id)
    # count how many existing fic parts there are in the set
    count = existing_part_numbers.count()

    # format the existing fic parts...
    ordered_parts = existing_part_numbers.order_by(
        '-fic_part_number')
    # ...and extract their part numbers
    part_list = ordered_parts.values_list(
        'fic_part_number', flat=True)

    # checking part_list length fixes index out of range without changing current behavior
    # if this function is used outside of the save call, may want a 0 length part list to return None.
    if len(part_list) == 0 or (fic_part_number is None and part_list[0] is None):
        return 1
    elif ((fic_part_number == 0) or (fic_part_number == 1)) and count == 1:
        return 1
    elif fic_part_number >= count:
        try:
            fic_part.fic_part_number = fic_part_number
            fic_part.validate_unique()
        except ValidationError as e:
            return count+1
        else:
            return count
    elif fic_part_number < count:
        try:
            fic_part.fic_part_number = fic_part_number
            fic_part.validate_unique()
        except ValidationError as e:
            raise ValidationError('\
                The FicPart number is not unique. Please\
                change it to a unique number.')
        else:
            return fic_part_number
