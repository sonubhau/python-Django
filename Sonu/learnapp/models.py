from django.db import models

# Create your models here.
class Student(models.Model):
    Name = models.CharField(max_length=20,blank=False,null=False)
    Last_Name = models.CharField(max_length=20,blank=True,null=True)
    Roll_Number = models.IntegerField(max_length=10,blank=False,null=False)


