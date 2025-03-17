# Generated by Django 5.1.4 on 2025-02-16 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fapk', '0023_rename_price_cart_totalprice_remove_cart_category_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='prod',
            new_name='products',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='quantity',
            new_name='stock',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='prod',
            new_name='product',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='totalprice',
        ),
        migrations.AddField(
            model_name='cart',
            name='total',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='order_id',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='quantity',
            field=models.PositiveBigIntegerField(default=1),
        ),
    ]
