from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings
#from languages.fields import LanguageField

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
    studentcode = models.IntegerField(primary_key=True, serialize=False,
                                      verbose_name="Studentcode", null=False)
    year = models.CharField(
        max_length=6, choices=YEAR_CHOICES, default="1")
    name = models.CharField(max_length=140, verbose_name="first Name")
    surname = models.CharField(max_length=140)
    idcard = models.CharField(max_length=13)
    commencementday = models.DateField(
        blank=True, null=True, auto_now=False, auto_now_add=False)
    email = models.EmailField(max_length=140)
    telphoneNumber = models.CharField(max_length=10)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Skill(models.Model):
    skillid = models.AutoField(
        primary_key=True, serialize=False, verbose_name="SKILLID")
    studentname = models.ForeignKey(
        Student, related_name="skills", on_delete=models.CASCADE)
    name = models.CharField(
        max_length=140, choices=PROGRAMING_LANGUAGES, unique=True, verbose_name="SKILLNAME")
    score = models.DecimalField(default=0.0, validators=[
        MaxValueValidator(100), MinValueValidator(0)], max_digits=30, decimal_places=20, verbose_name="SKILLSCORE")
    sumscore = models.DecimalField(validators=[
        MaxValueValidator(100), MinValueValidator(0)], max_digits=30, decimal_places=0, blank=True, verbose_name="SKILLSUMSCORE")

    def save(self, *args, **kwargs):
        self.sumscore = round(int(self.score))
        super(Skill, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ["name"]


class Language(models.Model):
    languageid = models.AutoField(
        primary_key=True, serialize=False, verbose_name="LANGUAGEID")
    studentname = models.ForeignKey(
        Student, related_name="languages", on_delete=models.CASCADE)
    name = models.CharField(
        max_length=140, choices=LISTLANGUAGE_CHOICES, unique=True, verbose_name="LANGUAGENAME")
    score = models.DecimalField(default=0.0, validators=[
        MaxValueValidator(100), MinValueValidator(0)], max_digits=30, decimal_places=20, verbose_name="LANGSCORE")
    sumscore = models.DecimalField(validators=[
        MaxValueValidator(100), MinValueValidator(0)], max_digits=30, decimal_places=0, blank=True, verbose_name="LANGSUMSCORE")

    def save(self, *args, **kwargs):
        self.sumscore = round(int(self.score))
        super(Language, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ["name"]
