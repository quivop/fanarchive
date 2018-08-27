from django.test import TestCase

from fanfic.models import AuthorGroup, Authorship, Fic, FicPart, Pseud
from datetime import timedelta
from django.utils import timezone


class FicModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        #
        # Fic with default pub_date (fic1)

        Fic.objects.create(
            fic_title='Ermagerd',
            fic_summary="Really, erma freaking gard, they're sleeping together...",)
        # Fic with future pub_date (fic2)
        Fic.objects.create(
            fic_title='No really',
            fic_summary="What in the ACTUAL HELLO",
            pub_date=(timezone.now() + timedelta(days=1)),
            date_updated=(timezone.now() + timedelta(days=1)))
        # Fic part related to fic1 (fic_part1)
        FicPart.objects.create(
            fic_id=1,
            fic_part_title='Fits around me so tight',
            fic_part_text='No-o...')

    # Fic Tests
    def test_fic_name_is_fic_title(self):
        fic = Fic.objects.get(id=1)
        expected_name = '%s' % (fic.fic_title)
        self.assertEqual(expected_name, str(fic))

    def test_pub_date_is_today(self):
        # also checks that a default date is being set at all
        fic = Fic.objects.get(id=1)
        expected_date = timezone.now()
        delta = expected_date - fic.pub_date

        if delta.days < 0:
            self.assertTrue(False, msg="delta between pub_date and today is less than zero")
        else:
            self.assertTrue(delta.seconds < 86400, msg="pub_date is NOT today")

    def test_date_updated_is_today(self):
        # also checks that a default date is being set at all
        fic = Fic.objects.get(id=1)
        expected_date = timezone.now()
        delta = expected_date - fic.date_updated

        if delta.days < 0:
            self.assertTrue(False, msg="delta between date_updated and today is less than zero")
        else:
            self.assertTrue(delta.seconds < 86400, msg="date_updated is NOT today")

    # FicPart tests
    def test_fic_part_is_related_to_correct_fic(self):
        fic_part = FicPart.objects.get(id=1)
        fic_id = fic_part.fic_id
        self.assertEqual(fic_id, 1)

    def test_fic_part_name_is_fic_part_title(self):
        fic_part = FicPart.objects.get(id=1)
        expected_name = '%s' % (fic_part.fic_part_title)
        self.assertEqual(expected_name, str(fic_part))


# FUTURE TESTS #

# test that fic with future pub_date posts properly
# test that fic with past pub_date posts properly

# test that fics are sorted by date in reverse order?
