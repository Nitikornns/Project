# Generated by Django 3.1.5 on 2021-03-09 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='address',
            field=models.CharField(blank=True, max_length=140, null=True),
        ),
    ]
