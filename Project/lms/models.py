from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    phone_number = models.CharField(max_length=17, null=True, blank=False, unique=True)
    age = models.PositiveSmallIntegerField(null=True, blank=False)

    USER_TYPE_CHOICES = (
        (1, 'student'),
        (2, 'teacher'),
    )
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, null=True, blank=False)


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='student_profile')
    courses = models.ManyToManyField("Course", related_name='enrolled_students')


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='teacher_profile')
    courses = models.ManyToManyField("Course", related_name='taught_courses')


class Course(models.Model):
    name = models.CharField(max_length=50, null=True)
    description = models.TextField(blank=False, null=False)
    # relations
    # teacher
    teacher = models.ForeignKey("Teacher", on_delete=models.CASCADE, related_name='teacher_programs')
    def __str__(self) -> str:
        return self.name


class Exam(models.Model):
    course = models.ForeignKey("Course", on_delete=models.CASCADE, related_name='courses')
    time = models.PositiveSmallIntegerField(null=True)
    date = models.DateTimeField(null=True)
    def __str__(self) -> str:
        return f'{self.course.name} - {self.date}'
