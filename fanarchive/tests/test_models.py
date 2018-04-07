from django.test import TestCase

from fanarchive.models import Fic, FicPart
from datetime import date, timedelta


class FicModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        #
        # Fic with default date_created (fic1)
        Fic.objects.create(
            fic_title='Ermagerd',
            fic_summary="Really, erma freaking gard, they're sleeping together...",)
        # Fic with future date_created (fic2)
        Fic.objects.create(
            fic_title='No really',
            fic_summary="What in the ACTUAL HELLO",
            date_created=(date.today() + timedelta(days=1)))
        # Fic part related to fic1 (fic_part1)
        FicPart.objects.create(
            fic_id=1,
            fic_part_title='Fits around me so tight',
            fic_part_text='No-o...')

    # Fic Tests
    def test_fic_title_label(self):
        fic = Fic.objects.get(id=1)
        field_label = fic._meta.get_field('fic_title').verbose_name
        self.assertEquals(field_label, 'fic title')

    def test_fic_summary_label(self):
        fic = Fic.objects.get(id=1)
        field_label = fic._meta.get_field('fic_summary').verbose_name
        self.assertEquals(field_label, 'fic summary')

    def test_date_created_label(self):
        fic = Fic.objects.get(id=1)
        field_label = fic._meta.get_field('date_created').verbose_name
        self.assertEquals(field_label, 'date created')

    def test_object_name_is_fic_title(self):
        fic = Fic.objects.get(id=1)
        expected_object_name = '%s' % (fic.fic_title)
        self.assertEquals(expected_object_name, str(fic))

    def test_date_created_is_today(self):
        # also checks that a default date is being set at all
        fic = Fic.objects.get(id=1)
        expected_date = date.today()
        self.assertEquals(expected_date, fic.date_created)

    def test_fic_title_max_length(self):
        fic = Fic.objects.get(id=1)
        max_length = fic._meta.get_field('fic_title').max_length
        self.assertEquals(max_length, 200)

    # FicPart tests
    def test_fic_part_title_label(self):
        fic_part = FicPart.objects.get(id=1)
        field_label = fic_part._meta.get_field('fic_part_title').verbose_name
        self.assertEquals(field_label, 'fic part title')

    def test_fic_part_text_label(self):
        fic_part = FicPart.objects.get(id=1)
        field_label = fic_part._meta.get_field('fic_part_text').verbose_name
        self.assertEquals(field_label, 'fic part text')

    def test_fic_part_title_max_length(self):
        fic_part = FicPart.objects.get(id=1)
        max_length = fic_part._meta.get_field('fic_part_title').max_length
        self.assertEquals(max_length, 200)

    def test_fic_part_is_related_to_correct_fic(self):
        fic_part = FicPart.objects.get(id=1)
        fic_id = fic_part.fic_id
        self.assertEquals(fic_id, 1)


# FUTURE TESTS #

# test that fic with future date_created posts properly
# test that fic with past date_created posts properly

# test that fics are sorted by date in reverse order?

