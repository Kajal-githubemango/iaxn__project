# Generated by Django 4.1.3 on 2023-01-28 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_alter_pricemodel_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricemodel',
            name='price',
            field=models.CharField(max_length=100, verbose_name='model verbose name'),
        ),
    ]
