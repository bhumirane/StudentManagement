from django.db import models

# Create your models here.
class Student(models.Model):
    student_number = models.PositiveIntegerField()
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField(max_length=100)
    field_of_study = models.CharField(max_length=60)
    gpa = models.FloatField()

    def __str__(self) -> str:
        return f'Student: {self.first_name}{self.last_name}'
