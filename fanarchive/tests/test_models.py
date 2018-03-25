from django.test import TestCase

from fanarchive.models import Work
from datetime import date
import datetime

class WorkModelTest(TestCase):

	@classmethod
	def setUpTestData(cls):
		# Set up non-modified objects used by all test methods
		Work.objects.create(work_title='Ermagerd', work_summary="Really, erma freaking gard, they're sleeping together...",)

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

	def test_object_name_is_work_title(self):
		work=Work.objects.get(id=1)
		expected_object_name = '%s' % (work.work_title)
		self.assertEquals(expected_object_name,str(work))

	def test_date_created_is_today(self):
		# also checks that a default date is being set at all
		work=Work.objects.get(id=1)
		expected_date = date.today()
		self.assertEquals(expected_date, work.date_created)	

	def test_work_title_max_length(self):
		work=Work.objects.get(id=1)
		max_length = work._meta.get_field('work_title').max_length
		self.assertEquals(max_length,200)
