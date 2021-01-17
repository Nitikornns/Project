from django.db import models
# Create your models here.
from django.db.models import Exists
from django.core.validators import MaxValueValidator, MinValueValidator


YEAR_CHOICES = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
)

PROGRAMING_LANGUAGES = (
    ("Java", "Java"),
    ("Python", "Python"),
    ("Html", "Html"),
    ("C", "C"),
    ("JavaScript", "JavaScript"),
    ("C++", "C++"),
    ("C#", "C#"),
)


class Student(models.Model):
    studentcode = models.IntegerField(primary_key=True, serialize=False,
                                      verbose_name='Studentcode', null=False)
    year = models.CharField(max_length=6, choices=YEAR_CHOICES, default='1')
    name = models.CharField(max_length=140)
    surname = models.CharField(max_length=140)
    idcard = models.CharField(max_length=13)
    commencementday = models.DateField(
        null=True, auto_now=False, auto_now_add=False)
    email = models.EmailField(max_length=140)
    telphoneNumber = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Skill(models.Model):
    skillid = models.AutoField(
        primary_key=True, serialize=False, verbose_name='ID')
    studentname = models.ForeignKey(
        Student, related_name='skills', on_delete=models.CASCADE)
    languagename = models.CharField(
        max_length=140, choices=PROGRAMING_LANGUAGES)
    score = models.IntegerField(default=0, validators=[
        MaxValueValidator(5), MinValueValidator(0)])

    def __str__(self):
        return f"{self.languagename}"

    class Meta:
        ordering = ['languagename']
