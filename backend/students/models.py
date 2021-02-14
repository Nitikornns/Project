from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings
from django.db import models

DEGREE = (
    ("พื้นฐานเล็กน้อย", "พื้นฐานเล็กน้อย"),
    ("ปานกลาง", "ปานกลาง"),
    ("ดี", "ดี"),
    ("ดีเยี่ยม", "ดีเยี่ยม"),
    ("เชี่ยวชาญ", "เชี่ยวชาญ"),
)

EDUCATION_DEEGREE = (
    ("มัธยมศึกษา", "มัธยมศึกษา"),
    ("ประกาศนียบัตรวิชาชีพ (ปวช.)", "ประกาศนียบัตรวิชาชีพ (ปวช.)"),
    ("ประกาศนียบัตรวิชาชีพชั้นสูง (ปวส.)", "ประกาศนียบัตรวิชาชีพชั้นสูง (ปวส.)"),
    ("ปริญญาตรี", "ปริญญาตรี"),
    ("ปริญญาโท", "ปริญญาโท"),
    ("ปริญญาเอก", "ปริญญาเอก"),
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


LISTLANGUAGE_CHOICES = (
    ("กัมพูชา", "กัมพูชา"),
    ("กาตาร์", "กาตาร์"),
    ("เกาหลีใต้", "เกาหลีใต้"),
    ("เกาหลีเหนือ", "เกาหลีเหนือ"),
    ("คาซัคสถาน", "คาซัคสถาน"),
    ("คีร์กีซสถาน", "คีร์กีซสถาน"),
    ("คูเวต", "คูเวต"),
    ("จอร์เจีย", "จอร์เจีย"),
    ("จอร์แดน", "จอร์แดน"),
    ("จีน", "จีน"),
    ("ซาอุดีอาระเบีย", "ซาอุดีอาระเบีย"),
    ("ซีเรีย", "ซีเรีย"),
    ("ไซปรัส", "ไซปรัส"),
    ("ญี่ปุ่น", "ญี่ปุ่น"),
    ("ติมอร์ตะวันออกติมอร์-เลสเต", "ติมอร์ตะวันออกติมอร์-เลสเต"),
    ("ตุรกี", "ตุรกี"),
    ("เติร์กเมนิสถาน", "เติร์กเมนิสถาน"),
    ("ไต้หวัน", "ไต้หวัน"),
    ("ทาจิกิสถาน", "ทาจิกิสถาน"),
    ("ไทย", "ไทย"),
    ("เนปาล", "เนปาล"),
    ("บรูไน", "บรูไน"),
    ("บังกลาเทศ", "บังกลาเทศ"),
    ("บาห์เรน", "บาห์เรน"),
    ("ปากีสถาน", "ปากีสถาน"),
    ("ปาเลสไตน์", "ปาเลสไตน์"),
    ("ฝรั่งเศษ", "ฝรั่งเศษ"),
    ("พม่าเมียนมา", "พม่าเมียนมา"),
    ("ฟิลิปปินส์", "ฟิลิปปินส์"),
    ("ภูฏาน", "ภูฏาน"),
    ("มองโกเลีย", "มองโกเลีย"),
    ("มัลดีฟส์", "มัลดีฟส์"),
    ("มาเลเซีย", "มาเลเซีย"),
    ("เยเมน", "เยเมน"),
    ("ลาว", "ลาว"),
    ("เลบานอน", "เลบานอน"),
    ("เวียดนาม", "เวียดนาม"),
    ("ศรีลังกา", "ศรีลังกา"),
    ("สหรัฐอาหรับเอมิเรตส์", "สหรัฐอาหรับเอมิเรตส์"),
    ("สิงคโปร์", "สิงคโปร์"),
    ("อัฟกานิสถาน", "อัฟกานิสถาน"),
    ("อาเซอร์ไบจาน", "อาเซอร์ไบจาน"),
    ("อาร์มีเนีย", "อาร์มีเนีย"),
    ("อินเดีย", "อินเดีย"),
    ("อินโดนีเซีย", "อินโดนีเซีย"),
    ("อิรัก", "อิรัก"),
    ("อิสราเอล", "อิสราเอล"),
    ("อิหร่าน", "อิหร่าน"),
    ("อุซเบกิสถาน", "อุซเบกิสถาน"),
    ("โอมาน", "โอมาน"),
    ("อังกฤษ", "อังกฤษ"),
)


class Student(models.Model):
    studentid = models.AutoField(
        primary_key=True, serialize=False, verbose_name="StudentId")
    accountid = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=140, verbose_name="firstName")
    surname = models.CharField(max_length=140)
    idcard = models.CharField(max_length=13)
    commencementday = models.DateField(
        blank=True, null=True, auto_now=False, auto_now_add=False)
    email = models.EmailField(max_length=140)
    telphoneNumber = models.CharField(max_length=10)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ["name"]


class Skill(models.Model):
    accountid = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    skillid = models.AutoField(
        primary_key=True, serialize=False, verbose_name="SkillId")
    name = models.CharField(
        max_length=140, choices=PROGRAMING_LANGUAGES, verbose_name="SkillName")
    degree = models.CharField(
        choices=DEGREE, max_length=150, verbose_name="SkillDegree")

    def __str__(self):
        return f"{self.accountid}"

    class Meta:
        ordering = ["name"]


class Language(models.Model):
    accountid = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    languageid = models.AutoField(
        primary_key=True, serialize=False, verbose_name="LanguageId")
    name = models.CharField(
        max_length=140, choices=LISTLANGUAGE_CHOICES, verbose_name="LanguageName")
    degree = models.CharField(
        choices=DEGREE, max_length=150, verbose_name="LanguageDegree")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ["name"]


class Education(models.Model):
    accountid = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    educationid = models.AutoField(
        primary_key=True, serialize=False, verbose_name="EducationId")
    datestart = models.DateField()
    dateend = models.DateField()
    name = models.CharField(max_length=140, verbose_name="EducationName")
    degree = models.CharField(
        choices=EDUCATION_DEEGREE, max_length=150)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ["name"]


class Picture(models.Model):
    accountid = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pictureid = models.AutoField(
        primary_key=True, serialize=False, verbose_name="PictureId")
    picturefile = models.FileField(null=True)

    def __str__(self):
        return f"{self.pictureid}"

    class Meta:
        ordering = ["pictureid"]


class Work(models.Model):
    accountid = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    workid = models.AutoField(
        primary_key=True, serialize=False, verbose_name="WorkId")
    name = models.CharField(max_length=140, verbose_name="WorkName")
    detail = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.workid}"

    class Meta:
        ordering = ["workid"]
