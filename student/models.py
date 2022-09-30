import email
from unicodedata import name
from django.db import models

class StudentDetails(models.Model):
    student_id = models.IntegerField()
    name = models.CharField(max_length=25)
    age = models.IntegerField()
    email = models.CharField(max_length=25)

    def __str__(self):
        return self.name

