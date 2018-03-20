from django.db import models

# Work model

class Work(models.model):
	# work title CharField with generous length allowance
	work_title = models.CharField('work title', max_length=200)
	# work summary TextField with max-length enforced only at view level, not on db or in the model
	work_summary = models.TextField('work summary', max_length=500)
	# date created DateField with a default of today's date
	date_created = models.DateField('date created', default=date.today)

	
