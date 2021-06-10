# Generated by Django 3.2.4 on 2021-06-10 01:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0002_alter_location_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Traveler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('travelername', models.CharField(max_length=100)),
                ('review', models.CharField(max_length=300)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel.location')),
            ],
        ),
    ]
