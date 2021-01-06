from django.db import models
# Create your models here.
from django.db.models import Exists

YEAR_CHOICES = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
)


class Student(models.Model):
    userid = models.IntegerField(primary_key=True, serialize=False,
                                 verbose_name='Userid', null=False)
    year = models.CharField(max_length=6, choices=YEAR_CHOICES, default='1')
    name = models.CharField(max_length=140, unique=True)
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
