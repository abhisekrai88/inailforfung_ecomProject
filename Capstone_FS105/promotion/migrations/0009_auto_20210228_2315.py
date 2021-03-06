# Generated by Django 3.1.5 on 2021-02-28 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promotion', '0008_promotion_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='promotion',
            name='active',
            field=models.BooleanField(default=False, verbose_name='Is Active?'),
        ),
        migrations.AddField(
            model_name='promotion',
            name='discount_amt',
            field=models.FloatField(blank=True, null=True, verbose_name='Discount'),
        ),
    ]
