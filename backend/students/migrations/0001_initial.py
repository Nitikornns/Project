# Generated by Django 3.1.4 on 2021-01-06 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('userid', models.IntegerField(primary_key=True, serialize=False, verbose_name='Userid')),
                ('year', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], default='1', max_length=6)),
                ('name', models.CharField(max_length=140, unique=True)),
                ('surname', models.CharField(max_length=140)),
                ('idcard', models.CharField(max_length=13)),
                ('commencementday', models.DateField(null=True)),
                ('email', models.EmailField(max_length=140)),
                ('telphoneNumber', models.CharField(max_length=10)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
