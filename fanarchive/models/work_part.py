from django.db import models

class WorkPart(models.Model):
    work_part_title = models.CharField('work part title', max_length=200)
    work_part_text = models.TextField('work part text')

    # One WorkPart can have many Works, but a WorkPart can only have one Work
    work = models.ForeignKey('Work', on_delete=models.CASCADE)

    def __str__(self):
        # returns title of the WorkPart when called by __str__()
        return self.work_part_title
