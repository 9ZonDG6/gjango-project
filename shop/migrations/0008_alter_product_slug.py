# Generated by Django 5.0.6 on 2024-05-20 17:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('shop', '0007_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(max_length=150, unique=True),
        ),
    ]
