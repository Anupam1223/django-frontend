# Generated by Django 3.2.4 on 2021-06-10 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0003_traveler'),
    ]

    operations = [
        migrations.AlterField(
            model_name='traveler',
            name='location',
            field=models.CharField(max_length=100),
        ),
    ]