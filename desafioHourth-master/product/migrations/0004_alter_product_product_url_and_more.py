# Generated by Django 4.1 on 2022-08-05 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_product_total_sales'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_url',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_url_created_at',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_url_image',
            field=models.CharField(max_length=255),
        ),
    ]