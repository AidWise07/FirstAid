# Generated by Django 4.2.11 on 2024-11-15 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fapk', '0010_usereg_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='usereg',
            name='check_password',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
