from django.test import TestCase

from fanarchive.models import Work
from django.utils import timezone

class WorkModelTest(TestCase):

	@classmethod
	def setUpTestData(cls):
		# Set up non-modified objects used by all test methods
		Work.objects.create(work_title='Ermagerd', work_summary="Really, erma freaking gard, they're sleeping together...", date_created=timezone.now())

	# testing field labels~
	def test_work_title_label(self):
		work=Work.objects.get(id=1)
		field_label = work._meta.get_field('work_title').verbose_name
		self.assertEquals(field_label, 'work title')

	def test_work_summary_label(self):
		work=Work.objects.get(id=1)
		field_label = work._meta.get_field('work_summary').verbose_name
		self.assertEquals(field_label, 'work summary')

	def test_date_created_label(self):
		work=Work.objects.get(id=1)
		field_label = work._meta.get_field('date_created').verbose_name
		self.assertEquals(field_label, 'date created')
