# Generated by Django 3.1.5 on 2021-01-27 23:46

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('studentcode', models.IntegerField(primary_key=True, serialize=False, verbose_name='Studentcode')),
                ('year', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], default='1', max_length=6)),
                ('name', models.CharField(max_length=140, verbose_name='first Name')),
                ('surname', models.CharField(max_length=140)),
                ('idcard', models.CharField(max_length=13)),
                ('commencementday', models.DateField(blank=True, null=True)),
                ('email', models.EmailField(max_length=140)),
                ('telphoneNumber', models.CharField(max_length=10)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('skillid', models.AutoField(primary_key=True, serialize=False, verbose_name='SKILLID')),
                ('name', models.CharField(choices=[('Java', 'Java'), ('Python', 'Python'), ('Html', 'Html'), ('C', 'C'), ('JavaScript', 'JavaScript'), ('C++', 'C++'), ('C#', 'C#')], max_length=140, unique=True, verbose_name='SKILLNAME')),
                ('score', models.DecimalField(decimal_places=20, default=0.0, max_digits=30, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)], verbose_name='SKILLSCORE')),
                ('sumscore', models.DecimalField(blank=True, decimal_places=0, max_digits=30, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)], verbose_name='SKILLSUMSCORE')),
                ('studentname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skills', to='students.student')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('languageid', models.AutoField(primary_key=True, serialize=False, verbose_name='LANGUAGEID')),
                ('name', models.CharField(choices=[('กัมพูชา', 'กัมพูชา'), ('กาตาร์', 'กาตาร์'), ('เกาหลีใต้', 'เกาหลีใต้'), ('เกาหลีเหนือ', 'เกาหลีเหนือ'), ('คาซัคสถาน', 'คาซัคสถาน'), ('คีร์กีซสถาน', 'คีร์กีซสถาน'), ('คูเวต', 'คูเวต'), ('จอร์เจีย', 'จอร์เจีย'), ('จอร์แดน', 'จอร์แดน'), ('จีน', 'จีน'), ('ซาอุดีอาระเบีย', 'ซาอุดีอาระเบีย'), ('ซีเรีย', 'ซีเรีย'), ('ไซปรัส', 'ไซปรัส'), ('ญี่ปุ่น', 'ญี่ปุ่น'), ('ติมอร์ตะวันออกติมอร์-เลสเต', 'ติมอร์ตะวันออกติมอร์-เลสเต'), ('ตุรกี', 'ตุรกี'), ('เติร์กเมนิสถาน', 'เติร์กเมนิสถาน'), ('ไต้หวัน', 'ไต้หวัน'), ('ทาจิกิสถาน', 'ทาจิกิสถาน'), ('ไทย', 'ไทย'), ('เนปาล', 'เนปาล'), ('บรูไน', 'บรูไน'), ('บังกลาเทศ', 'บังกลาเทศ'), ('บาห์เรน', 'บาห์เรน'), ('ปากีสถาน', 'ปากีสถาน'), ('ปาเลสไตน์', 'ปาเลสไตน์'), ('ฝรั่งเศษ', 'ฝรั่งเศษ'), ('พม่าเมียนมา', 'พม่าเมียนมา'), ('ฟิลิปปินส์', 'ฟิลิปปินส์'), ('ภูฏาน', 'ภูฏาน'), ('มองโกเลีย', 'มองโกเลีย'), ('มัลดีฟส์', 'มัลดีฟส์'), ('มาเลเซีย', 'มาเลเซีย'), ('เยเมน', 'เยเมน'), ('ลาว', 'ลาว'), ('เลบานอน', 'เลบานอน'), ('เวียดนาม', 'เวียดนาม'), ('ศรีลังกา', 'ศรีลังกา'), ('สหรัฐอาหรับเอมิเรตส์', 'สหรัฐอาหรับเอมิเรตส์'), ('สิงคโปร์', 'สิงคโปร์'), ('อัฟกานิสถาน', 'อัฟกานิสถาน'), ('อาเซอร์ไบจาน', 'อาเซอร์ไบจาน'), ('อาร์มีเนีย', 'อาร์มีเนีย'), ('อินเดีย', 'อินเดีย'), ('อินโดนีเซีย', 'อินโดนีเซีย'), ('อิรัก', 'อิรัก'), ('อิสราเอล', 'อิสราเอล'), ('อิหร่าน', 'อิหร่าน'), ('อุซเบกิสถาน', 'อุซเบกิสถาน'), ('โอมาน', 'โอมาน'), ('อังกฤษ', 'อังกฤษ')], max_length=140, unique=True, verbose_name='LANGUAGENAME')),
                ('score', models.DecimalField(decimal_places=20, default=0.0, max_digits=30, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)], verbose_name='LANGSCORE')),
                ('sumscore', models.DecimalField(blank=True, decimal_places=0, max_digits=30, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)], verbose_name='LANGSUMSCORE')),
                ('studentname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='languages', to='students.student')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('educationid', models.AutoField(primary_key=True, serialize=False, verbose_name='EDUCATIONID')),
                ('datestart', models.DateField()),
                ('dateend', models.DateField()),
                ('schoolname', models.CharField(max_length=140, verbose_name='School Name')),
                ('detail', models.CharField(blank=True, max_length=1000)),
                ('studentname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='education', to='students.student')),
            ],
            options={
                'ordering': ['schoolname'],
            },
        ),
    ]
