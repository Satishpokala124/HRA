# Generated by Django 3.1 on 2020-08-07 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='contact',
            field=models.CharField(max_length=10),
        ),
    ]
