# Generated by Django 4.2.11 on 2024-11-15 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fapk', '0008_product_sellercontact_product_sellermail_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='cart',
            name='sellercontact',
            field=models.IntegerField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cart',
            name='sellermail',
            field=models.EmailField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cart',
            name='sellername',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
