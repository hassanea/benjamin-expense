# Generated by Django 2.1.7 on 2019-03-27 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0003_expense_end_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expense',
            old_name='duration',
            new_name='recurrences',
        ),
    ]
