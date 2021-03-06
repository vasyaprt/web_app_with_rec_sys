# Generated by Django 3.2.3 on 2021-05-21 19:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('email', models.EmailField(max_length=254)),
                ('description', models.TextField(verbose_name='О себе')),
                ('img', models.ImageField(blank=True, upload_to='media/')),
            ],
        ),
        migrations.AddField(
            model_name='tour',
            name='price',
            field=models.CharField(blank=True, default=0, max_length=30, null=True, verbose_name='Цена'),
        ),
        migrations.AddField(
            model_name='tour',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.DecimalField(decimal_places=2, max_digits=4)),
                ('type', models.CharField(default='explicit', max_length=8)),
                ('tour_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ratings', to='main.tour')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ratings', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='main.tour')),
            ],
        ),
        migrations.AddField(
            model_name='tour',
            name='guide',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tours', to='main.guide'),
        ),
    ]
