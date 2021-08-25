# Generated by Django 3.2.3 on 2021-06-18 20:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0018_views'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.BooleanField(default=False)),
                ('time', models.TextField(blank=True)),
                ('msg', models.TextField(blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='tour',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Название'),
        ),
        migrations.DeleteModel(
            name='OrderHis',
        ),
        migrations.AddField(
            model_name='order',
            name='tour',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='main.tour'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to=settings.AUTH_USER_MODEL),
        ),
    ]
