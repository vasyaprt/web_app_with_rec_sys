# Generated by Django 3.2.3 on 2021-05-30 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_sim_tour'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sim_tour',
            name='sim_tours',
        ),
        migrations.AddField(
            model_name='sim_tour',
            name='sim_tours',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]