# Generated by Django 3.2.4 on 2021-06-10 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0004_alter_traveler_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='traveler',
            name='image',
            field=models.ImageField(default='', upload_to='images/'),
        ),
    ]