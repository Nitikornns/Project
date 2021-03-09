from django.db import models
from django.conf import settings
from django.db import models
import datetime

YEAR_CHOICES = [(r, r) for r in range(1900, datetime.date.today().year+1)]

EDUCATION_DEEGREE = (
    ("มัธยมศึกษา", "มัธยมศึกษา"),
    ("ประกาศนียบัตรวิชาชีพ (ปวช.)", "ประกาศนียบัตรวิชาชีพ (ปวช.)"),
    ("ประกาศนียบัตรวิชาชีพชั้นสูง (ปวส.)", "ประกาศนียบัตรวิชาชีพชั้นสูง (ปวส.)"),
    ("ปริญญาตรี", "ปริญญาตรี"),
    ("ปริญญาโท", "ปริญญาโท"),
    ("ปริญญาเอก", "ปริญญาเอก"),
)


class Info(models.Model):
    infoid = models.AutoField(
        primary_key=True, serialize=False, verbose_name="InfoId")
    accountid = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=140, verbose_name="firstName")
    surname = models.CharField(max_length=140)
    email = models.EmailField(max_length=140)
    telphoneNumber = models.CharField(max_length=10)
    address = models.CharField(max_length=140, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["name"]


class Skill(models.Model):
    accountid = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    skillid = models.AutoField(
        primary_key=True, serialize=False, verbose_name="SkillId")
    name = models.CharField(
        max_length=140, verbose_name="SkillName")
    detail = models.CharField(
        max_length=1000, verbose_name="SkillDetail", null=True, blank=True)

    class Meta:
        ordering = ["name"]


class Work(models.Model):
    accountid = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    workid = models.AutoField(
        primary_key=True, serialize=False, verbose_name="WorkId")
    name = models.CharField(
        max_length=140, verbose_name="WorkName")
    detail = models.CharField(
        max_length=1000, verbose_name="WorkDetail", null=True, blank=True)

    class Meta:
        ordering = ["name"]


class Talent(models.Model):
    accountid = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    talentid = models.AutoField(
        primary_key=True, serialize=False, verbose_name="TalentId")
    name = models.CharField(
        max_length=140, verbose_name="TalentName")
    detail = models.CharField(
        max_length=1000, verbose_name="TalentDetail", null=True, blank=True)

    class Meta:
        ordering = ["name"]


class Hobby(models.Model):
    accountid = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    hobbyid = models.AutoField(
        primary_key=True, serialize=False, verbose_name="HobbyId")
    name = models.CharField(
        max_length=140, verbose_name="HobbyName")

    class Meta:
        ordering = ["name"]


class Education(models.Model):
    accountid = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    educationid = models.AutoField(
        primary_key=True, serialize=False, verbose_name="EducationId")
    datestart = models.IntegerField(
        choices=YEAR_CHOICES, verbose_name="EducationDateStart", null=True)
    dateend = models.IntegerField(
        choices=YEAR_CHOICES, verbose_name="EducationDateEnd", null=True)
    name = models.CharField(max_length=140, verbose_name="EducationName")
    degree = models.CharField(
        choices=EDUCATION_DEEGREE, max_length=150)

    class Meta:
        ordering = ["name"]


class Picture(models.Model):
    accountid = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pictureid = models.AutoField(
        primary_key=True, serialize=False, verbose_name="PictureId")
    picturefile = models.FileField(null=True)

    class Meta:
        ordering = ["pictureid"]


class Experience(models.Model):
    accountid = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    experienceid = models.AutoField(
        primary_key=True, serialize=False, verbose_name="ExperienceId")
    datestart = models.IntegerField(
        choices=YEAR_CHOICES,  verbose_name="ExperienceDateStart", null=True)
    dateend = models.IntegerField(
        choices=YEAR_CHOICES, verbose_name="ExperienceDateEnd", null=True)
    name = models.CharField(max_length=140, verbose_name="ExperienceName")
    detail = models.CharField(
        max_length=1000, verbose_name="ExperienceDetail", null=True, blank=True)

    class Meta:
        ordering = ["experienceid"]
