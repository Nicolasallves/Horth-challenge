# Generated by Django 4.0.6 on 2022-08-04 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_url_image', models.CharField(max_length=255)),
                ('product_url', models.CharField(max_length=255)),
                ('product_url_created_at', models.CharField(max_length=255)),
                ('vendas_no_dia', models.CharField(blank=True, max_length=50, null=True)),
                ('consult_date', models.DateField(null=True)),
            ],
        ),
    ]
