# Generated by Django 3.1.5 on 2021-02-08 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_auto_20210208_0059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(max_length=500, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_ID',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='Product ID'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_type',
            field=models.CharField(max_length=100, verbose_name='Product Type'),
        ),
    ]