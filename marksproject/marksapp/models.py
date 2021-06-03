from django.db import models

# Create your models here.
class Student(models.Model):
    Name = models.CharField(max_length=64)
    Section = models.IntegerField()
    Email = models.EmailField()
    Marks_obtained = models.IntegerField()
    