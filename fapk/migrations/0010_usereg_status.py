# Generated by Django 4.2.11 on 2024-11-15 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fapk', '0009_cart_image_cart_sellercontact_cart_sellermail_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usereg',
            name='status',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
