# Generated by Django 3.2.3 on 2021-05-30 12:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20210530_1552'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sim_tour',
            old_name='tour1',
            new_name='tour',
        ),
    ]
