# Generated by Django 2.1.7 on 2019-03-27 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0004_auto_20190327_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='recurrences',
            field=models.IntegerField(default=0),
        ),
    ]