# Generated by Django 3.1.5 on 2021-02-08 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promotion', '0006_auto_20210208_0059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promotion',
            name='Promotion_ID',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='Promotion ID'),
        ),
        migrations.AlterField(
            model_name='promotion',
            name='promo_description',
            field=models.CharField(max_length=500, verbose_name='Promotion Description'),
        ),
        migrations.AlterField(
            model_name='promotion',
            name='promo_type',
            field=models.CharField(max_length=300, verbose_name='Promotion Type'),
        ),
    ]