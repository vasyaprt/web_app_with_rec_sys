# Generated by Django 3.2.3 on 2021-05-22 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20210522_0314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='view',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
