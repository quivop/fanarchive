from django.test import TestCase

from fanarchive.models import Work, WorkPart
from datetime import date, timedelta


class WorkModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        #
        # Work with default date_created (work1)
        Work.objects.create(
            work_title='Ermagerd',
            work_summary="Really, erma freaking gard, they're sleeping together...",)
        # Work with future date_created (work2)
        Work.objects.create(
            work_title='No really',
            work_summary="What in the ACTUAL HELLO",
            date_created=(date.today() + timedelta(days=1)))
        # Work part related to work1 (work_part1)
        WorkPart.objects.create(
            work_id=1,
            work_part_title='Fits around me so tight',
            work_part_text='No-o...')

    # Work Tests
    def test_work_title_label(self):
        work = Work.objects.get(id=1)
        field_label = work._meta.get_field('work_title').verbose_name
        self.assertEquals(field_label, 'work title')

    def test_work_summary_label(self):
        work = Work.objects.get(id=1)
        field_label = work._meta.get_field('work_summary').verbose_name
        self.assertEquals(field_label, 'work summary')

    def test_date_created_label(self):
        work = Work.objects.get(id=1)
        field_label = work._meta.get_field('date_created').verbose_name
        self.assertEquals(field_label, 'date created')

    def test_object_name_is_work_title(self):
        work = Work.objects.get(id=1)
        expected_object_name = '%s' % (work.work_title)
        self.assertEquals(expected_object_name, str(work))

    def test_date_created_is_today(self):
        # also checks that a default date is being set at all
        work = Work.objects.get(id=1)
        expected_date = date.today()
        self.assertEquals(expected_date, work.date_created)

    def test_work_title_max_length(self):
        work = Work.objects.get(id=1)
        max_length = work._meta.get_field('work_title').max_length
        self.assertEquals(max_length, 200)

    # WorkPart tests
    def test_work_part_title_label(self):
        work_part = WorkPart.objects.get(id=1)
        field_label = work_part._meta.get_field('work_part_title').verbose_name
        self.assertEquals(field_label, 'work part title')

    def test_work_part_text_label(self):
        work_part = WorkPart.objects.get(id=1)
        field_label = work_part._meta.get_field('work_part_text').verbose_name
        self.assertEquals(field_label, 'work part text')

    def test_work_part_title_max_length(self):
        work_part = WorkPart.objects.get(id=1)
        max_length = work_part._meta.get_field('work_part_title').max_length
        self.assertEquals(max_length, 200)

    def test_work_part_is_related_to_correct_work(self):
        work_part = WorkPart.objects.get(id=1)
        work_id = work_part.work_id
        self.assertEquals(work_id, 1)


# FUTURE TESTS #

# test that work with future date_created posts properly
# test that work with past date_created posts properly

# test that works are sorted by date in reverse order?


