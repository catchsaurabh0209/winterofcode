from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class organization(models.Model):
	user = models.ForeignKey(User, default=1,on_delete=models.CASCADE)
	org_name = models.CharField(max_length=250)
	
	def __str__(self):
		return self.org_name


class student(models.Model):
	user = models.ForeignKey(User, default=1,on_delete=models.CASCADE)
	student_name = models.CharField(max_length=250)
	
	def __str__(self):
		return self.student_name

