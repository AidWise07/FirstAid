# Generated by Django 5.1 on 2024-10-26 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fapk', '0004_doctor_doctoreg_remove_usereg_profilepic_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='manufacturer',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
