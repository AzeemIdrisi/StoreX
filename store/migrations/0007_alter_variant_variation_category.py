# Generated by Django 4.2.7 on 2023-11-22 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_variant_variation_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variant',
            name='variation_category',
            field=models.CharField(choices=[('Color', 'Color'), ('Size', 'Size')], max_length=100),
        ),
    ]
