from django.db import models

# Create your models here.
class UserModel(models.Model):
	Full_Name = models.CharField(max_length=50)
	Location = models.CharField(max_length=150)
	No_of_WorkDaysPerWeek = models.IntegerField()
