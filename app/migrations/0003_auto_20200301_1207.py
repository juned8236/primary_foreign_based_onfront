# Generated by Django 3.0.3 on 2020-03-01 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200228_2020'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product_id',
            new_name='company',
        ),
    ]