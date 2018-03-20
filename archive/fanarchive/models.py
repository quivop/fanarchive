from django.db import models

# Work model

class Work(models.Model):
	# work title CharField with generous length allowance
	work_title = models.CharField('work title', max_length=200)
	# work summary TextField with max-length enforced only at view level, not on db or in the model
	work_summary = models.TextField('work summary', max_length=500)
	# date created DateField with a default of today's date
	date_created = models.DateField('date created', default=date.today)

	def __str__(self):
		# returning a nice, human-readable representation of the model when called by __str__() method
		return self.work_title

# WorkPart model

class WorkPart(models.Model):
	# work part title CharField with generous length allowance
	work_part_title = models.CharField('work part title', max_length=200)
	# work part text TextField
	work_part_text = models.TextField('work part text')

	# Foreign key relating each WorkPart to one Work.
	# One WorkPart can have many Works, but a WorkPart can only have one Work
	work = models.ForeignKey(Work, on_delete=models.CASCADE)

	def __str__(self):
		# returns a human-readable representation of a WorkPart when called by __str__()
		return self.work_part_title