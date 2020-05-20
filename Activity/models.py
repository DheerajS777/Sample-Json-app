from django.db import models

# Create your models here.
class Activity_Data(models.Model):
	Member_id = models.CharField(max_length=50)
	Location = models.CharField(max_length=50)
	StartTime_Shift1  = models.CharField(max_length=50)
	StartTime_Shift2 = models.CharField(max_length=50)
	StartTime_Shift3 = models.CharField(max_length=50)
# Create your models here.
