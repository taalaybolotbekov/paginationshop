# Generated by Django 3.1.2 on 2020-10-03 05:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20201002_1352'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('name',), 'verbose_name_plural': 'shops_name'},
        ),
    ]