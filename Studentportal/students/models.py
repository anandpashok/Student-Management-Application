from django.db import models

class Student(models.Model):
    roll_number=models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    marks = models.IntegerField(null=True)



