from django.db import models

# Create your models here.

class todo(models.Model):
    taskname = models.CharField(max_length=100)
    taskdate = models.DateField()
    

