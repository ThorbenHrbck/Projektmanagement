# Generated by Django 4.2.19 on 2025-03-06 20:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Projektmanagement', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='created_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
