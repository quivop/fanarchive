from django.db import models
from django.db import models
from datetime import date

# WorkPart model

class WorkPart(models.Model):
	# work part title CharField with generous length allowance
	work_part_title = models.CharField('work part title', max_length=200)
	# work part text TextField
	work_part_text = models.TextField('work part text')

	# Foreign key relating each WorkPart to one Work.
	# One WorkPart can have many Works, but a WorkPart can only have one Work
	work = models.ForeignKey('Work', on_delete=models.CASCADE)

	def __str__(self):
		# returns a human-readable representation of a WorkPart when called by __str__()
		return self.work_part_title
