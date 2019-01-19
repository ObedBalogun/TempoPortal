from django.db import models
from django.utils import timezone


VISIT_TYPE=(('', 'Select Visit Type'),('Personal','Personal'),
('Official/Business','Official/Business'))

class Staff(models.Model):
    staff_name = models.CharField(max_length=250)
    staff_email = models.CharField(max_length=250, default="")

    def __str__(self):
        return self.staff_name

class Visitor(models.Model):
    visitor_name = models.CharField(max_length=250)

    def __str__(self):
        return '{}'.format(self.visitor_name)

class VisitRequests(models.Model):
    staff=models.ForeignKey(Staff, on_delete=models.CASCADE)
    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE)
    comment= models.TextField(default='')
    status= models.NullBooleanField()
    token=models.CharField(max_length=30)
    timestamp = models.DateTimeField('created',auto_now_add=True)
    visit_type = models.CharField(max_length=50,choices=VISIT_TYPE,default='SELECT VISIT TYPE')



    def __str__(self):
        return '{}'.format(self.staff)
