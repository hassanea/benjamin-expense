# Generated by Django 2.1.7 on 2019-04-05 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0010_auto_20190405_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='color',
            field=models.CharField(choices=[('none', 'None'), ('red', 'Red'), ('blue', 'Blue'), ('green', 'Green'), ('yellow', 'Yellow')], default='none', max_length=6),
        ),
    ]