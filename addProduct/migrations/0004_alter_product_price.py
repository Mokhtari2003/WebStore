# Generated by Django 5.1.7 on 2025-04-01 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addProduct', '0003_remove_product_productid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Price',
            field=models.DecimalField(decimal_places=1, max_digits=9),
        ),
    ]
