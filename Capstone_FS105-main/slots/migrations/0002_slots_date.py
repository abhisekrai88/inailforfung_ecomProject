# Generated by Django 3.1.4 on 2021-02-18 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slots', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='slots',
            name='date',
            field=models.DateField(blank=True, null=True),
            preserve_default=False,
        ),
    ]
