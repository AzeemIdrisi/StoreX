# Generated by Django 4.2.7 on 2023-11-22 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_alter_variant_variation_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variant',
            name='variation_value',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
