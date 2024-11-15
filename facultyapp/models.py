from django.db import models
from django.contrib.auth.models import User
from adminapp.models import StudentList


class AddCourse(models.Model):
    COURSE_CHOICES = [
        ('AOOP','ADVANCED Object-Oriented Programming'),
        ('PFSD','Python Full Stack Development'),
        ('DBMS','Database Management System'),
        ('LAA','Linux Administration'),
    ]
    SECTION_CHOICES = [
        ('S11', 'Section-21'),
        ('S12', 'Section-22'),
        ('S13', 'Section-23'),
        ('S14', 'Section-24'),
        ('S15', 'Section-25'),
    ]
    student = models.ForeignKey(StudentList, on_delete=models.CASCADE)
    course = models.CharField(max_length=50, choices=COURSE_CHOICES)
    section = models.CharField(max_length=50, choices=SECTION_CHOICES)
    def __str__(self):
        return f'{self.student.Register_Number} {self.course} ({self.section})'

class Marks(models.Model):
    COURSE_CHOICES = [
        ('AOOP','ADVANCED Object-Oriented Programming'),
        ('PFSD','Python Full Stack Development'),
    ]
    student = models.ForeignKey(StudentList, on_delete=models.CASCADE)
    course = models.CharField(max_length=50, choices=COURSE_CHOICES)
    Marks = models.IntegerField()
    def __str__(self):
        return f"{self.student.name} - {self.course}"

from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=100, default='Anonymous')  # Default value for name
    email = models.EmailField(default='example@example.com')  # Default value for email
    phone_number = models.CharField(max_length=15, blank=True)  # Optional phone number
    description = models.TextField()  # Renamed field
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])  # Rating from 1 to 5
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically adds timestamp

    def __str__(self):
        return f'Feedback from {self.name} - Rating: {self.rating}'
