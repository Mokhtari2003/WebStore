# Generated by Django 5.1.7 on 2025-04-02 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addProduct', '0005_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Price',
            field=models.IntegerField(max_length=15),
        ),
    ]
