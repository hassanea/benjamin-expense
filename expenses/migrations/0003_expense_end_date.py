# Generated by Django 2.1.7 on 2019-03-23 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0002_auto_20190323_2034'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
