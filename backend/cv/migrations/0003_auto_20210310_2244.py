# Generated by Django 3.1.5 on 2021-03-10 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0002_auto_20210309_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='degree',
            field=models.CharField(choices=[('มัธยมศึกษาตอนต้น', 'มัธยมศึกษาตอนต้น'), ('มัธยมศึกษาตอนปลาย', 'มัธยมศึกษาตอนปลาย'), ('ประกาศนียบัตรวิชาชีพ (ปวช.)', 'ประกาศนียบัตรวิชาชีพ (ปวช.)'), ('ประกาศนียบัตรวิชาชีพชั้นสูง (ปวส.)', 'ประกาศนียบัตรวิชาชีพชั้นสูง (ปวส.)'), ('ปริญญาตรี', 'ปริญญาตรี'), ('ปริญญาโท', 'ปริญญาโท'), ('ปริญญาเอก', 'ปริญญาเอก')], max_length=150),
        ),
    ]
