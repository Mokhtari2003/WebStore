# Generated by Django 5.1.7 on 2025-04-02 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addProduct', '0004_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Image',
            field=models.ImageField(upload_to='ProductImage/'),
        ),
    ]
