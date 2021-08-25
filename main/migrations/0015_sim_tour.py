# Generated by Django 3.2.3 on 2021-05-30 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20210530_1509'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sim_tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sim_tours', models.ManyToManyField(blank=True, related_name='score', to='main.Tour')),
                ('tour1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='seachtour', to='main.tour')),
            ],
        ),
    ]
